---
layout: page
title:  pirt-unitによるi2cデバイスの利用
---

<!-- Title: PiRT-UnitによるI2Cデバイスの利用 -->
#contents

## はじめに

Raspberry Pi上に存在する GPIO ピンのうちのI2C用ピン(2本)を用いると、複数の I2C デバイスを操作することができます。
ここでは、I2C を利用するためのセットアップ、C言語によるプログラム記述の実例、RTコンポーネント化するためのヒントを示します。

### 必要なもの

- OpenRTM-aist の C++版がインストールされた Raspberry Pi
- I2C デバイスを配線するための資材（ブレッドボード、ケーブル、抵抗、他）
- I2C デバイス（秋月、ストロベリーリナックス、スイッチサイエンス等で入手）
- ネットワーク(インターネット、apt-get するため）

このドキュメントでは、I2C デバイスとして、
- [LSM303DLHC（3軸地磁気＋加速度センサ）](http://strawberry-linux.com/catalog/items?code=12114)
- [L3GD20（3軸ジャイロセンサ）](http://strawberry-linux.com/catalog/items?code=12120)
- [RTC-8564NB（リアルタイムクロック）](http://akizukidenshi.com/catalog/g/gI-00233/)
- [MPL115A2（大気圧センサ）](http://strawberry-linux.com/catalog/items?code=12103)

を取り上げます。

## I2C(アイ・スクエア・シー)とは

I2C は2線を用いるシリアルバス通信の一種です。クロック線のエッジを用いてデータ線上で値の授受行い、バス上にある複数デバイスを制御することができます。
バス上にはマスターとスレーブがあり、規格では複数のマスター／スレーブの存在を許しているようですが、実際には単一マスター／複数スレーブによる使用が簡単です。
マイコンなどから利用する場合は、マスターによるクロック信号の送信と、データの通信プロトコル実装などを考慮して実装しなければなりませんが、Raspberry Pi を用いると既存のライブラリを使用して非常に簡単に I2C デバイスを利用することができます。

Raspberry Pi の GPIOポート(26pin)のうち、もともと I2C 通信専用に設定されている GPIO が2本存在します。（下図参照）
GPIO 0 が I2C のデータ用ポート、GPIO 1 が I2C のクロック用ポートとしてあらかじめ設定されており、これらを利用することで簡単に I2C 通信を行うことができます。

<div align="center"><a href="raspberry_gpio.png"><img src="raspberry_gpio.png" width="80%;"></a></div>
<div align="center"><strong>Raspberry PiのGPIOポート、GPIO0 (I2C SDA), GPIO1 (I2C SCL)</strong></div>

この2本のポートを用いて I2C デバイスを直接接続するだけで、クロック線のドライブ・通信プロトコルの解釈などはすべて Raspberry Pi上の Linux で行われます。
ユーザーはデバイスファイル (/dev/i2c-*) の読み書きを行うことでデバイスからのデータ取得／デバイスへのデータ出力を実現できます。

複数のデバイスの接続はバス接続（下図）で実現することができます。
デバイス間の調停も Raspberry Pi側である程度は行うことになっています。
なお、上記GPIO 0、GPIO 1ポートは Raspberry Pi 基板上でプルアップ抵抗によりプルアップされていますので、別途プルアップする必要はありません。

<div align="center"><a href="i2c_devices.png"><img src="i2c_devices.png" width="80%;"></a></div>
<div align="center"><strong>I2Cバス接続</strong></div>

## 準備

### システム設定

Raspberry Pi で I2C 通信を使うためにはいくつのかの設定ファイルを変更する必要があります。
ファイルは root 権限で編集してください。

#### /etc/modules の編集
/etc/modules に以下の一行を追加します。

```
 i2c-dev
```

これにより、/dev/i2c-* が有効になります。

#### /etc/modprobe.d/raspi-blacklist.conf の編集

/etc/modprobe.d/raspi-blacklist.conf の以下の一行をコメントアウトします。

```
 # blacklist i2c-bcm2708
```


以上の変更が終了したら、変更を反映するために再起動してください。

### i2c-tools のインストール

i2c-tools はコマンドラインから I2C デバイスへアクセスするためのツールです。
実際に開発する際には、コマンドラインから I2C デバイスの動作を確認したいことがたびたびありますので、事前に i2c-tools をインストールしておいてください。

```
 sudo apt-get install i2c-tools
```

として、インストールします。

## 配線

上記のブロック図では、I2C デバイスは SDA、SCL の2線のみが配線されていましたが、実際には当然各デバイスに電源を供給してあげる必要があります。
それほど消費電力の大きくない I2C デバイスであれば、Raspberry Pi の GPIO ピンヘッダ 26pin のうち、2,3pin(5V)、1,17pin(3.3V)からでている電源を利用することができます。
I2C デバイスの説明書・データシートを参照した上で、5V ないし 3.3V のうち適切な電源を供給するようにしてください。
また、PiRT-Unit には I2C用の4ピンのコネクタが付属しており、SDA、SCL、3.3V、GND が配線可能です。

今回用いる I2C デバイスはすべて 3.3V で動作するため、Raspberry Pi の 1,17pin(3.3V)から各デバイスに電源を供給します。
以下にブレッドボード上に上記の4つのデバイスを配置した際の配線図を示します。

<div align="center"><a href="i2c_devices_circuit.png"><img src="i2c_devices_circuit.png" width="80%;"></a></div>
<div align="center"><strong>I2CデバイスとRaspberryPiの接続</strong></div>

配線の際にはデバイスの説明書／データシートをよく読んで間違いのないよう配線してください。配線を間違うとデバイスが認識されないだけでなく、場合によってはデバイスが破壊される可能性もあります。

デバイスの種類によっては、使用方法によって適宜ジャンパが必要なものや、I2Cの2本の信号線以外に割り込み、リセット信号などをが必要なものもあります。その場合は、Raspberry Pi の GPIO ピンを適宜利用し、プログラム側から制御する必要があります。

## 動作確認

### デバイスアドレスの確認

上記の配線が完了したら、Raspberry Pi上から i2c-tools を利用してデバイスを操作することができます。
まずは、**i2cdetect** コマンドで、I2C バスに接続されているすべてのデバイスのアドレスを確認してみましょう。以下のようにタイプすると、下図のような表示が現れます。

```
 $ sudo i2cdetect 1
```


<div align="center"><a href="i2c_i2ctools_i2cdetect.png"><img src="i2c_i2ctools_i2cdetect.png" width="80%;"></a></div>
<div align="center"><strong>I2CデバイスとRaspberryPiの接続</strong></div>

図では4個のデバイスが存在していることが確認できます。**-(マイナス)**以外に16進数の数字が表示されていますが、それぞれが各デバイスのアドレスを表しています。内訳は、

- 0x19：LSM303DLHCの加速度センサー
- 0x1e：LSM303DLHCの地磁気センサー
- 0x51：RTC-8564NB（リアルタイムクロック）
- 0x6a：L3GD20（ジャイロセンサー）

となっています。このコマンドと各デバイスの説明書／データシートを突き合わせることで、Raspberry Pi が I2C デバイスを認識できているかを確認することができます。
なお、Raspberry Pi のリビジョンによって、コマンドの後ろに入れるバス番号が0の場合と1の場合がありますので注意してください。

### デバイスの制御テスト

デバイスに実際にデータを書き込むには **i2cset** コマンドを、デバイスからデータを読み込むには**i2cget**コマンドを使用します。（下図参照）

<div align="center"><a href="i2c_i2ctest.png"><img src="i2c_i2ctest.png" width="60%;"></a></div>
<div align="center"><strong>i2ctestコマンドによるI2Cデバイスの制御の様子</strong></div>

```
 // LSM303DLHCの地磁気センサーへアクセス
 $ sudo i2cset -y 1 0x1e 0x00 0x14
 $ sudo i2cset -y 1 0x1e 0x01 0x20
 $ sudo i2cset -y 1 0x1e 0x02 0x00
 $ sudo i2cget -y 1 0x1e 0x32
 $ sudo i2cget -y 1 0x1e 0x31
 $ sudo i2cget -y 1 0x1e 0x03
 $ sudo i2cget -y 1 0x1e 0x04
 $ sudo i2cget -y 1 0x1e 0x05
 $ sudo i2cget -y 1 0x1e 0x06
 $ sudo i2cget -y 1 0x1e 0x07
 $ sudo i2cget -y 1 0x1e 0x08
 $ sudo i2cget -y 1 0x1e 0x09
 // LSM303DLHCの加速度センサーへアクセス
 $ sudo i2cset -y 1 0x19 0x20 0x27
 $ sudo i2cget -y 1 0x19 0x28
 $ sudo i2cget -y 1 0x19 0x29
 $ sudo i2cget -y 1 0x19 0x2a
 $ sudo i2cget -y 1 0x1e 0x2b
 $ sudo i2cget -y 1 0x1e 0x2c
 $ sudo i2cget -y 1 0x1e 0x2d
```

この例では、LSM303DLHCの説明書に従って、まず地磁気センサを動作させるために0x1eのアドレスのデバイスに対して内部レジスタ0x00～0x02に所定の数値を書き込み、内部レジスタ0x31～32、0x03～0x09を読み出しています。
その後、LSM303DLHCの加速度センサを動作させるため、0x19のアドレスのデバイスに対して内部レジスタ0x20に所定の数値を書き込み、0x28～0x2dまでの数値を読み込んでいます。

i2c-toolsのコマンド群はルート権限でのみ実行可能であるのでsudoを使用するか、sudo bashとしてrootになって実行する必要がありますので注意してください。


## C言語によるデバイス操作

プログラムからこれらのデバイスにアクセスするには、デバイスファイル (/dev/i2c-0 または /dev/i2c-1) をオープンし、読み書きすることでデバイスのレジスタ操作および値の読み出しを行います。

ただし、I2Cデバイスの種類によっては特有の初期化シーケンスを持っていたり、デバイスのデータの読み書きに一定の手順を要求するものがあります。各デバイスの説明書やデータシートを確認しながらプログラムを作成する必要があります。
（インターネット上には、RaspberryPi／AVRマイコン／ArduinoなどからのI2Cデバイスの制御方法に関する情報が色々あるようですので、そちらも参考にしてください。）

以下に、L3GD20デジタル3軸ジャイロセンサモジュールを用いたサンプルプログラムを掲載します。

このモジュールはI2CおよびSPIでの通信が可能なセンサモジュールで、I2Cデバイスとして利用する場合、アドレスを0x6a、0x6bの2種類から選択可能です。ここではアドレスを0x6aとして使用しています。

内部レジスタは、
<table class="table-alt">
  <tr>
    <th>0x0f</th>
    <th>常に0xd4を出力</th>
  </tr>
  <tr>
    <td>0x20</td>
    <td>0x0fを書き込むことで動作開始</td>
  </tr>
  <tr>
    <td>0x28～2d</td>
    <td>3軸ジャイロデータが格納される</td>
  </tr>
</table>

このほか、検出レンジ、サンプリングレート等の設定も可能ですが、ここでは触れません。

### プログラム

以下にプログラムを示します。
なお、こちらからダウンロードすることもできます。また、I2CセンサをRTコンポーネント化した、データ取得コンポーネントおよびディスプレイコンポーネントもサンプルとして示します。

- ジャイロL3GD20テストプログラム: [i2c_gyrotest.c](i2c_gyrotest.c)
- I2Cセンサデータ取得コンポーネント: [Pi_I2CSensor.zip](Pi_I2CSensor.zip)
- I2Cセンサディスプレイコンポーネント: [Pi_SensorDataOutPut.zip](Pi_SensorDataOutPut.zip)


```
 #include <stdio.h>
 #include <stdlib.h>
 #include <time.h>
 #include <unistd.h>
 
 #include <linux/i2c-dev.h> // I2C用インクルード
 #include <fcntl.h>
 #include <sys/ioctl.h>
 
 #include <wiringPi.h> // delay関数用にインクルード
 
 // プロトタイプ宣言
 void L3GD20_readData(int *gyrodata, int fd);
 void L3GD20_write(unsigned char address, unsigned char data, int fd);
 unsigned char L3GD20_read(unsigned char address, int fd);
 void L3GD20_init(int fd);
 
 int main(int argc, char **argv)
 {
 	int i2c_fd;       // デバイスファイル用ファイルディスクリプタ
    // char *i2cFileName = "/dev/i2c-0"; // I2Cデバイスファイル名
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
 	//デバイス初期化
 	L3GD20_init(i2c_fd);
 	
 	// 1秒ごとに20回ジャイロデータを取得、表示
 	int i;
 	for(i=0; i<20; i++){
 		// デバイスからデータ取得
 		L3GD20_readData(gyroData, rtc); 
 		// 取得したデータを校正して表示、1秒待ち
 		printf("x, y, z : %5.2f, %5.2f, %5.2f\n",
               (float)gyroData[0]*0.00875,(float)gyroData[1]*0.00875,
               (float)gyroData[2]*0.00875);
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
 		exit(1);
    }
 	return;
 }
   
 // L3GD20用 1バイト読み出しルーチン： addressで示すレジスタの値を読み出す
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
 
 // L3GD20用 ジャイロデータ読み出しルーチン：
 // 整数値配列へのポインタを使ってデータを受け渡す
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
 	Data = L3GD20_read(0x20,fd); if(Data != 0x0f){
 		printf("Writing miss\n");
 		exit(1);
 	} 
 	printf("Writing OK\n");
 	delay(10); 	
 	return;
 }
```


## RTコンポーネント化のためのヒント

RaspberryPi上でI2Cデバイスにアクセスするプログラムは以上のように記述することができます。上記のコードをRTコンポーネント化する場合には、例えば初期化部分をRTコンポーネントの**onInitialize**または**onActivated**に実装、デバイスからデータを取得して表示するルーチンを **onExecute** に実装し、OutPortから出力するようにすれば、センサデータを出力するコンポーネントが出来上がります。

実行コンテキストの周期は、I2Cデバイスおよびバスの速度と、バスに接続されているI2Cデバイスの数、それぞれのI2Cデバイスのサンプリングレートなどから決める必要があります。

複数のデバイスをI2C接続した状態でこれらをコンポーネント化する場合、各デバイス間でデータの読み書きのスケジューリングを考慮する必要があります。
実現手法として考えられるのは、
- すべてのI2Cデバイスを一つのコンポーネントとして取り扱う
- I2Cバスへのアクセスを単一コンポーネントにまかせ、個別デバイスからポート間通信でデータを取得する
- ロックなどの排他制御を共有オブジェクトなどを使って実装する
などが考えられますが、それぞれ一長一短があるので状況に応じて選択するのがよいでしょう。


