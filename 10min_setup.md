
## 10���Ŏn�߂悤



<a name="startup_openrtm"></a>
�ŐV�o�[�W���� OpenRTM-aist-1.1.2-RELEASE �ł� C++�ŁAPython�ŁAJava�ł���x�ɃC���X�g�[���ł���悤�ɂȂ�܂����B �܂��A����܂ŕʓr�C���X�g�[�����Ă��� rtshell �������ɃC���X�g�[���\�ɂȂ�܂����B

### Python 2.7 �C���X�g�[��

Python 2.7 ���C���X�g�[�����Ă��Ȃ��ꍇ�́AOpenRTM-aist �̓C���X�g�[���ł��܂���B��� Python2.7 ���C���X�g�[�����Ă��������B

�C���X�g�[���̍ۂ́A�uAdd python.exe to Path�v�̐ݒ��ύX���A�uWill be installed on local hard drive�v��I�����Ă��������B
��������ƁApython.exe �� Scripts �� PATH ��ʂ��Ă���܂��B�@�i��FPath=C:\Python27\;C:\Python27\Scripts;...�j

![Python 2.7 PATH��ʂ�](./images/10min_setup/python27_install.jpg)


### OpenRTM-aist �C���X�g�[��


�����ł�32bit�p�C���X�g�[���[ OpenRTM-aist-1.1.2-RELEASE_x86.msi ���g�����菇���Љ�܂��B �C���X�g�[���[�̃_�E�����[�h�́AOpenRTM-aist-1.1.2-RELEASE<�����N> ���������������B

1. �C���X�g�[���[���N�����A[����] ���N���b�N���܂��B

![](./images/10min_setup/install1.png)

2. �g�p�����_�񏑂̃y�[�W�ł��B�\�t�g�E�F�A���C�Z���X�����ɓ��ӂ��āA[����] ���N���b�N���܂��B

![](./images/10min_setup/install2.png)

3. �C���X�g�[���̎�ނ�I�����܂��B�ǂ��炩��I�����āA[����] ���N���b�N���܂��B 

![](./images/10min_setup/install3.png)

4. �Z�b�g�A�b�v�̎�ނ�I�����܂��B[�W��] ��I�������ꍇ�AOpenRTM-aist �� C++�ŁAJava�ŁAPython�ŁAOpenRTP�ARTSystemEditorRCP�ARTShell�AOpenRTM-aist-C++�ł� Visual Studio 2008 ���� 2015 �܂ł̃����^�C�����C�u�����AOpenRTM-aist-1.0.0 ���� 1.1.1 �܂ł̃����^�C�����C�u�������C���X�g�[������܂��B���ɕύX���R���Ȃ��悤�ł���΁A[�W��] ���N���b�N���܂��B

![](./images/10min_setup/install4.png)

5. [�C���X�g�[��] ���N���b�N����ƃC���X�g�[�����J�n���܂��B 

![](./images/10min_setup/install5.png)

![](./images/10min_setup/install6.png)

6. �C���X�g�[�����I�����܂����B[����] ���N���b�N���ăC���X�g�[���[���I�����܂��B

![�C���X�g�[���I�����](./images/10min_setup/install7.png)

���g�p���Ă��� Visual Studio �̃o�[�W������2013(vc12)�ȊO�̏ꍇ�́A���ϐ��� RTM_VC_VERSION ��ύX���Ă��������B


### �T���v���R���|�[�l���g�����s����

�K�{�ł͂���܂��񂪁A��������̓X�^�[�g���j���[�ɓo�^���ꂽ�A�v���P�[�V�����𑽐��N�����܂��B����X�^�[�g���j���[���珇�Ԃɂ��ǂ�̂͑�ςł��̂ŁA


![�t�@�C���̏ꏊ���J��](./images/10min_setup/install8.png)

�X�^�[�g��ʂ̍������̖�󂩂�A�v���r���[��\�����āAOpenRTM-aist-1.1.2 �� OpenRTP �ŉE�N���b�N���A[�t�@�C���̏ꏊ���J��] ��I�����Ă��������B

������1��̃t�H���_�[�Ɉړ����Ă��������B

![�X�^�[�g���j���[�t�H���_�[](./images/10min_setup/install31.png)

���̂悤�ɁA�X�^�[�g���j���[�̃t�H���_�[���J����A�l�X�ȃA�v���P�[�V�����ɃA�N�Z�X���₷���Ȃ�܂��B �ł́A�C���X�g�[�����ꂽ�T���v���R���|�[�l���g�����s���Ă݂܂��B

#### ConsoleInComp�AConsoleOutComp���g�p����

ConsoleInComp�AConsoleOutComp �� DataInPort�ADataOutPort �̎g�p���@���������T���v���ł��BConsoleIn ���œ��͂����������CConsoleOut ���ɕ\������܂��B

##### rtm-naming�N��

[OpenRTM-aist 1.1.2] > [Tools] �� Start Naming Service ���N���b�N���ċN�����܂��B

![Start Naming Service](./images/10min_setup/install30.png)

##### �T���v���R���|�[�l���g�N��

[OpenRTM-aist 1.1.2] > [C++] > [Components] > [Examples] �� ConsoleInComp.exe �� ConsoleOutComp.exe ���N���b�N����ƃR���\�[����ʂ��N�����܂��B 

![ConsoleInComp.exe��ConsoleOutComp.exe](./images/10min_setup/install29.png)

##### OpenRTP�N��

�������� OpenRTP �𑀍삵�܂��B[OpenRTM-aist 1.1.2] > [Tools] �� OpenRTP ���N���b�N���ċN�����܂��B ���[�N�X�y�[�X�͓K���ȏꏊ���w�肵�Ă��������B

![���[�N�X�y�[�X�̑I��](./images/10min_setup/install40.png)

�u�悤�����v��ʂ͍��̂Ƃ���K�v�Ȃ��̂ō���� [�悤����] �^�u�� [�~] �{�^�����N���b�N���ĉ�ʂ���Ă��������B

![�����N�����̉��](./images/10min_setup/install41.png)

�E��́u�p�[�X�y�N�e�B�u���J���v���N���b�N���A�uRT System Editor�v��I�����邱�ƂŁARTSystemEditor ���N�����܂��B

![](./images/10min_setup/install42.png)
![�p�[�X�y�N�e�B�u�̐؂�ւ�](./images/10min_setup/install43.png)


��NameServerView �Ƀl�[���T�[�o�[���\������Ȃ����́A�蓮�� localhost ��ǉ����܂��B�摜�� [�l�[���T�[�o�̒ǉ�] ���N���b�N���_�C�A���O��\�����܂��Blocalhost �Ɠ��͂��A[OK] ���N���b�N���Ēǉ����܂��B

![�l�[���T�[�o�̒ǉ�](./images/10min_setup/install44.png)

NameServiceView �ɃR���|�[�l���g���\������܂��B�ŏ��͐܂肽���܂�Ĕ�\���ł��B[>] ���N���b�N���W�J����ƁAConsoleInComp�AConsoleOutComp�R���|�[�l���g���m�F�ł��܂��B

![�R���|�[�l���g�N���m�F](./images/10min_setup/install45.png)

[OpenNewSystemEditor] ���N���b�N���āASystemDiagram ��\�����܂��B

![SystemDiagram��\��](./images/10min_setup/install46.png)

NameServiceView �̃R���|�[�l���g���V�X�e���E�_�C�A�O�����Ƀh���b�O���h���b�v����Ɖ摜�̂悤�ɕ\������܂��B

![�R���|�[�l���g���h���b�O���h���b�v](./images/10min_setup/install47.png)

�R���|�[�l���g��ڑ����܂��B�f�[�^�|�[�g�ԂŃh���b�O���h���b�v��A�ڑ��ɕK�v�ȏ��̓��͂𑣂��_�C�A���O���\�������̂ŁA[OK] ���N���b�N���܂��B

![�R���|�[�l���g�ڑ�](./images/10min_setup/install48.png)
![�R���|�[�l���g�ڑ�](./images/10min_setup/install49.png)

�ڑ����������܂����B

![�ڑ�����](./images/10min_setup/install50.png)

�R���|�[�l���g�̏�Ԃ� Activate �ɂ��܂��B[All Activate] �N���b�N���Ă��������B�R���|�[�l���g�̐F�����疾�邢�΂ɕς�����琬���ł��B�R���|�[�l���g�͌ʂɑI������ Activate �ɂ��邱�Ƃ��\�ł��B

![Activate����](./images/10min_setup/install51.png)
![Activate����](./images/10min_setup/install52.png)

���ɃR���\�[����ʂœ���m�F���܂��BRTSystemEditor �Őڑ���AConsoleInComp.exe �R���\�[���ɁA�uPlease input number:�v�ƕ\������܂��B

![ConsoleInComp.exe��ConsoleOutComp.exe](./images/10min_setup/install24.png)

ConsoleInComp.exe �R���\�[����ʂ�I�����A���l����͂� [Enter] �������ƁAConsoleOutComp.exe �R���\�[���ɐ��l���\������܂��B

![����m�F](./images/10min_setup/install25.png)
![����m�F](./images/10min_setup/install26.png)

�����l�ȊO�̓��͂�A�傫�����鐔�l����͂���ƃG���[(��)�ɂȂ�܂��B ���R���|�[�l���g���G���[���N��������ARTSystemEditor �ŃR���|�[�l���g���E�N���b�N���� Reset ��I�����Ă��������B


�ȏ�� ConsoleInComp.exe �� ConsoleOutComp.exe ���g�p��������m�F�͏I���ł��B�R���|�[�l���g���I������ꍇ�́ADeactivate ���Ă��� Exit ���ĉ������B

![�R���|�[�l���g��A�N�e�B�u��](./images/10min_setup/install53.png)

![�R���|�[�l���g�I��](./images/10min_setup/install54.png)

��Deactivate �Ɏ��Ԃ�������ꍇ�� ConsoleInComp.exe �̐��l���͂Ŏ~�܂��Ă���̂ŁA�������l����͂��Ă��������B

### rtshell �𗘗p����

OpenRTM-aist-1.1.2 �ł� rtshell ���W���ŃC���X�g�[������܂��B rtshell �𗘗p���邱�ƂŃR�}���h���C������ RTC �̃A�N�e�B�u���A��A�N�e�B�u���A�I�������ł���悤�ɂȂ�܂��B

��64bit�ł��C���X�g�[�������ꍇ�� dll �̕s���ɂ�蓮��ł��Ȃ��ꍇ������܂��B���̏ꍇ�� Windows Update �����s���Ă��������B

#### RTC �̑���

�T���v���R���|�[�l���g���N�����Artshell �ɂ��R�}���h���C������f�[�^�|�[�g�̐ڑ��ARTC �̃A�N�e�B�u���A��A�N�e�B�u���A�I�����s���܂��B


##### rtm-naming�N��

[OpenRTM-aist 1.1.2] > [Tools] �� Start Naming Service ���N���b�N���ċN�����܂��B

##### �T���v���R���|�[�l���g�N��

�܂��̓T���v���R���|�[�l���g���N�����āA�N�������R���|�[�l���g�� rtshell �ő��삵�܂��B [OpenRTM-aist 1.1.2] > [Python] > [Components] > [Examples] ��ConsoleIn.py �� ConsoleOut.py ���N���b�N����ƃR���\�[����ʂ��N�����܂��B

ConsoleIn.py�AConsoleOut.py �� ConsoleInComp.exe�AConsoleOutComp.exe �̊�{�I�ȓ���͓����ł��B

##### �R�}���h�v�����v�g����̑���

���ɃR�}���h�v�����v�g���N�����Ă��������B

![�R�}���h�v�����v�g�̋N��](./images/10min_setup/install32.png)

�܂��AC:\Python27\Scripts �Ƀp�X��ݒ肵�Ă��Ȃ��ꍇ�͈ȉ��̃R�}���h�Ńp�X��ݒ肵�Ă��������B

    set PATH=C:\Python27\Scripts;%PATH%

���Ɉȉ��̃R�}���h�Ńf�[�^�|�[�g��ڑ����܂��B

    rtcon /localhost/ConsoleIn0.rtc:out /localhost/ConsoleOut0.rtc:in

����� ConsoleIn.py�AConsoleOut.py �R���\�[���Ɉȉ��̂悤�ȕ����񂪕\������܂��B

   ------------------------------
   Listener:        ON_CONNECT
   Profile::name:   outin
   Profile::id:     4d622f80-135f-11e6-b923-001c4231a7a3
   ------------------------------

![�f�[�^�|�[�g�ڑ��̕\��](./images/10min_setup/install36.png)

�O�̂��߂� RT�V�X�e���G�f�B�^�Ŋm�F���܂��B
NameServiceView �̃R���|�[�l���g���V�X�e���E�_�C�A�O�����Ƀh���b�O���h���b�v����ƁA �f�[�^�|�[�g���ڑ����ꂽ���Ƃ��m�F�ł��܂��B


![�f�[�^�|�[�g�ڑ��̊m�F](./images/10min_setup/install55.png)

�����Ĉȉ��̃R�}���h�� RTC ���A�N�e�B�u�����܂��B

    rtact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc

�A�N�e�B�u���ɐ������Ă���� ConsoleIn.py �R���\�[���ɁA�uPlease input number:�v�ƕ\������܂��B

RT�V�X�e���G�f�B�^�����Ă݂�ƁARTC ���A�N�e�B�u�����ꂽ���Ƃ��m�F�ł��܂��B

![�A�N�e�B�u���̊m�F](./images/10min_setup/install56.png)

������ ConsoleIn.py �R���\�[����ʂŐ��l����͂���ƁAConsoleOut.py �R���\�[���ɐ��l���\������܂��B

![ConsoleIn.py �� ConsoleOut.py](./images/10min_setup/install38.png)

�ȉ��̃R�}���h�� RTC ���A�N�e�B�u�����Ă��������B

   rtdeact /localhost/ConsoleIn0.rtc /localhost/ConsoleOut0.rtc
��ConsoleIn ����A�N�e�B�u���ł��Ȃ��ꍇ�A���l���͂Ŏ~�܂��Ă���̂ŉ������l����͂��Ă��������B

�Ō�Ɉȉ��̃R�}���h�� RTC ���I�������Ă��������B

   rtexit /localhost/ConsoleIn0.rtc
   rtexit /localhost/ConsoleOut0.rtc
