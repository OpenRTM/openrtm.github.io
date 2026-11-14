#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#include <linux/i2c-dev.h> // I2C用インクルード
#include <fcntl.h>
#include <sys/ioctl.h>

#include <wiringPi.h> // delay関数用にインクルード

void L3GD20_readData(int *gyrodata, int fd);
void L3GD20_write(unsigned char address, unsigned char data, int fd);
unsigned char L3GD20_read(unsigned char address, int fd);
void L3GD20_init(int fd);

int main(int argc, char **argv)
{
	int i2c_fd;       // デバイスファイル用ファイルディスクリプタ
//  char *i2cFileName = "/dev/i2c-0"; // I2Cデバイスファイル名
	char *i2cFileName = "/dev/i2c-1"; // RaspberryPiのリビジョンに合わせて変更
	int i2cAddress = 0x6a;   // L3GD20のI2Cアドレス
	int gyroData[3]; // ジャイロ3軸（x,y,z）データ格納用
	
	printf("i2c Gyro(L3GD20) test program\n");
	delay(500);

	// I2Cデバイスファイルをオープン
	if ((i2c_fd = open(i2cFileName, O_RDWR)) < 0) 
	{
		printf("Faild to open i2c port\n");
		exit(1);
	}
	// L3GD20用にセット
	if (ioctl(i2c_fd, I2C_SLAVE, i2cAddress) < 0) 
	{
		printf("Unable to get bus access to talk to slave\n");
		exit(1);
	}

	//デバイスイニシャライズ
	L3GD20_init(i2c_fd);
	
	// 1秒ごとに20回ジャイロデータを取得、表示
	int i;
	for(i=0; i<20; i++){
		// デバイスからデータ取得
		L3GD20_readData(gyroData, rtc); 
		// 取得したデータを校正して表示、1秒待ち
		printf("x, y, z : %5.2f, %5.2f, %5.2f\n",(float)gyroData[0]*0.00875,(float)gyroData[1]*0.00875,(float)gyroData[2]*0.00875);
		delay(1000); 
	}
	return;
}

// L3GD20用 1バイト書き込みルーチン：addressで示すレジスタにdataを書き込む
void L3GD20_write(unsigned char address, unsigned char data, int fd)
{
	unsigned char buf[2];
	buf[0] = address;
	buf[1] = data;
	if((write(fd,buf,2))!=2){
		printf("Error writing to i2c slave\n");
		exit(1);}
	return;
}
  
// L3GD20用 1バイト読み出しルーチン：addressで示すレジスタの値を読み出す
// 戻り値がレジスタ値
unsigned char L3GD20_read(unsigned char address, int fd)
{
	unsigned char buf[1];
	buf[0] = address;
	if((write(fd,buf,1))!= 1){ // addressを一度書き込む所に注意
		printf("Error writing to i2c slave\n");
		exit(1);}
	if(read(fd,buf,1)!=1){
		printf("Error reading from i2c slave\n");
		exit(1);}
	return buf[0];
}

// L3GD20用 ジャイロデータ読み出しルーチン：整数値配列へのポインタを使ってデータを受け渡す
void L3GD20_readData(int *gyrodata, int fd)
{
	unsigned char data[6];
	// センサから3軸に対して2バイトずつデータを読み出す
	int i;
	for(i=0; i<6; i++){
		data[i]=L3GD20_read(0x28+i,fd);
	}
	// 各数値を32bit幅の整数に整形する
	// センサの数値精度が16bit・2の補数表現での出力のため、シフトで加工
	gyrodata[0]=((int)data[1]<<24|(int)data[0]<<16)>>16;
	gyrodata[1]=((int)data[3]<<24|(int)data[2]<<16)>>16;
	gyrodata[2]=((int)data[5]<<24|(int)data[4]<<16)>>16;
	return;
}

// L3GD20用 ジャイロデータイニシャライズルーチン
void L3GD20_init(int fd)
{
	unsigned char Data;
	printf("L3GD20 init seq. start\n");
	// L3GD20 動作確認
	// L3GD20の0x0fレジスタは常に0xd4にセットされているため動作確認ができる
	Data = L3GD20_read(0x0f,fd);
	if(Data != 0xd4){
		printf("L3GD20 is not working\n");
		exit(1);}
	delay(10);
	// レジスタへの書き込みチェックとイニシャライズを同時に行う
	printf("read OK, Now writing check...\n");
	// 0x20レジスタに0x0fを書き込むことで動作させる
	L3GD20_write(0x20, 0x0f, fd);
	// 0x20レジスタに実際に0x0fが書かれたか確認
	Data = L3GD20_read(0x20,fd);
	if(Data != 0x0f){
		printf("Writing miss\n");
		exit(1);
	} 
	printf("Writing OK\n");
	delay(10);
	return;
}
 