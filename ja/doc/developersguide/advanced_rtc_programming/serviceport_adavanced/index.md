---
layout: page
title: "サービスポート (応用編)"
---
<!-- Title: サービスポート (応用編) -->
#contents

## IDL 文法
### 構造体 / オブジェクトリファレンス 

CORBA の構造体は、以下のように C++ の構造体 "struct" にマッピングされます。
<!-- -*- IDL -*- -->
```
 struct Profile
 {
 
	short short_value;
	long  long_value;
  
 };
```

```
 // -*- C++ -*-
 struct Profile
 {
 
	CORBA::Short short_value;
	CORBA::Long  long_value;
 
 };
```

```
 class Profile_var
 {
  
 };
```

- 固定長の構造体と可変長の構造体<br>
下記に示す、構造体に可変長のメンバーが含まれていると、構造体は可変長データとみなされます。
この場合、固定長の構造体とは異なる C++ コードが生成され、戻り値や out パラメーターにおける扱いが異なります。
  - 制限付き文字列または無制限文字列
  - 制限付きシーケンスまたは無制限シーケンス
  - 可変長メンバーを含む構造体またはユニオン
  - 可変長の要素型を持つ配列
  - 可変長型へのtypedef

上記の一覧に型が該当しない場合、その型は固定長になります。 

- _var型 IDLコンパイラは IDLにおける構造体から、C++ の構造体と _var 型のクラスを自動的に生成します。 _var 型クラスはスマートポインタのように振る舞い、可変長の構造体として _var クラスを使用する場合、可変長のメンバーに割り当てられるメモリーは自動的に管理されます。 _var 型の変数(var1)から他の_var型の変数(var2)に代入が行われた場合には、そのポインタの所有権が var2 に移り、その後 var1 は初期化もしくは代入が行われるまで使用することはできません。
<br><br>
- 構造体がスコープの外に出ると，可変長のメンバーに関連付けられていたすべてのメモリーは自動的に解放されます。 ただし、すでに所有権を他に譲渡している_var型変数がスコープから出る場合、所有権を既に譲渡しているので、元のデータに対しては開放は行われません。
<br><br>
- 初期化もしくは代入された構造体に対して、再び初期化または代入が行われた場合、元のデータに関連付けられていたメモリーは自動的に解放されます。
<br><br>
- 可変長のメンバーにオブジェクトリファレンスが代入される場合は、必ずそのオブジェクトリファレンスのコピーが作成されます。可変長のメンバーにポインタが代入される場合、コピーは作成されません。


### _var型
#### 変換コンストラクタ(T_ptr)

- 実装例

```
 _CORBA_ObjRef_Var(T_ptr p) : pd_objref(p) {}
```

_ptr型のオブジェクト参照の所有権は_var型に移るため、参照カウントは増減しません。

```
 MyObject_ptr ptr = obj->get_myobject();
 // ptr は適切なタイミングで release されなければならない
 
 MyObject_var var(ptr); 
 // 所有権は var に移ったため、ptr をリリースする必要はない
 // var がスコープを抜けるなどして解体されると、参照カウントは release される
 
```
#### 変換コンストラクタ(const T_var&)
- 実装例

```
 Object_var(const T_var& p) : pd_ref(T::_duplicate(p.pd_ref)) {}
```

代入元の_var型のオブジェクト参照の所有権はコピーされます。

```
 MyObject_var var0 = obj->get_myobject();  // var0 は所有権を持つ
 MyObject_var var1(var0);  // リファレンスカウントはインクリメントされ var1も所有権を持つ
```

#### 変換コンストラクタ(const T_member) 
- 実装例

#### in引数と in()関数
単純にオブジェクト参照の_ptr型ポインタを返します。所有権は移行されません。

- 実装例

```
 T_ptr  in() const { return pd_objref; }
```

通常、関数の in 引数にオブジェクト参照を渡す際に使用します。
オブジェクト参照を与えられた側の関数は、所有権を持たないため関数内で release してはいけません。
関数から戻ってきたあと、_var型変数に依然として所有権が保持されており、_var型変数の解体時にオブジェクトは release されます。

オブジェクト参照を in 引数として受け取る関数を定義する場合は、_ptr型の引数として定義します。
さらに、関数内では、そのオブジェクトのオペレーションを呼ぶだけで、release 等は行ってはいけません。
また、関数内でオブジェクト参照をどこか(グローバル変数、static変数、オブジェクトのメンバー等)に保存したい場合は、所有権をコピーするため duplicate関数で複製する必要があります。

- 使用例

```
 void myfunc(MyObject_ptr obj)
 {
 
	obj->function();
	CORBA::release(obj); // ×これはしてはいけない
	m_obj = obj; // ×所有権を持っていない
	m_obj = MyObject::duplicate(obj); // ○所有権を複製
 
 }
 
 {// 別のコンテキスト 
 
	MyObject_var obj(hoge->get_object());
	myfunc(obj.in()); // 所有権は移行されない
 
 }
 // スコープを抜けたので参照カウントがデクリメントされる
```

#### out引数と out()関数 
現在所有している参照を release して、リファレンスのポインタを nil にセットして返します。
すなわち、out()関数呼び出し以前にもしオブジェクト参照を保持している場合は、その所有権を放棄し参照は破棄されます。

- 実装例

```
 T_ptr& out()
 {
	T_Helper::release(pd_objref);
	pd_objref = T_Helper::_nil();
	return pd_objref;
 }
```

通常、関数の out引数にオブジェクト参照を渡す際に使用します。
すなわち、関数から戻ってきたあと、この変数に新たにオブジェクト参照が保持されていることが期待されます。
このとき、オブジェクト参照の所有権はこの変数に保持されていると考えます。
out() で変数を渡された関数側では、何らかの形でオブジェクト参照を生成または複製して、引数に所有権を渡す必要があります。

オブジェクト参照を out引数として受け取る関数を定義する場合は、_ptr型参照の引数として定義します。
関数内では、引数は必ずnilオブジェクト参照であり、かつ通常何らかのオブジェクトを所有権を与えて代入することが期待されます。

- 使用例

```
 void myfunc(MyObject_ptr& obj)
 {
	assert(CORBA::is_nil(obj)); // 必ず nil オブジェクトを指定する
	obj->function(); // nil なのでオペレーションは呼べない
 
	// m_obj は_var型のメンバ変数
	obj = m_obj; // ×所有権を複製していない。
	// return後、関数の外で勝手に release されるかもしれない。
 
	obj = MyObject::duplicate(obj); // ○所有権を複製している。
	// return後、関数の外で release されても、オブジェクト参照は解体されない。
	return;
 }
 
 {// 別のコンテキスト
	MyObject_var obj;
	obj = get_object(); // △out変数として使うので渡す前には何も入れない方がよい
	myfunc(obj.out());
	// オブジェクトが代入され返ってきたはず
	assert(!CORBA::is_nil(obj));
	obj->function();
 }
 // スコープを抜けたので参照カウントがデクリメントされる。
 
```
#### inout()
リファレンスへのポインタの参照を返します。

- 実装
```
 T_ptr& inout()    { return pd_objref; }
```

通常、関数の inout引数にオブジェクト参照を渡す際に使用します。
すなわち、関数内では何らかのオブジェクト参照が引数に入っていることが期待され、オブジェクトの所有権は関数側に移行します。
また、関数は何らかのオブジェクト参照をこの引数に与えて返すことが期待され、引数すなわち呼び出し元の変数に所有権を与えます。
関数内では引数にオブジェクト参照を新たにセットする場合は、まず release してから新たなオブジェクト参照を生成または複製して引数に所有権を渡す必要があります。

オブジェクト参照を inout引数として取る関数は、設計の観点からあまり推奨されません。
もし、inout引数として取る関数を定義する必要がある場合は、_ptr型参照の引数として定義します。

- 使用例

```
 void myfunc(MyObject_ptr& obj)
 {
	if (!CORBA::is_nil(obj))
	{
		obj->function(); // obj が nil でなければオペレーションを呼ぶことができる。
	}
   
	CORBA::release(obj); // releaseする責任はこの関数にある
	/*
	* この関数内で、obj に新たなオブジェクト参照がある場合に限り、
	* 引数を受け取った直後に、_var変数に代入しておくことで、
	* 関数終了時に自動的に参照カウントをデクリメント
	* するテクニックを使用してもよい。
	* MyObject_var deleter = obj;
	*/
  
	// MyObject_var m_obj とする
	obj = m_obj; // × 所有権を複製していない
	// return 後、関数の外で release されるかもしれない。
	obj = MyObject::_duplicate(m_obj); // ○ obj にも MyObject の所有権が与えられた
	// return 後、関数の外で release されても、オブジェクト参照は解体されない。
 }
  
 {// 別のコンテキスト
	MyObject_var obj;
	obj = get_object(); // obj は所有権を持っている
	myfunc(obj); // 関数内で releae される
	// obj の指すものは入れ替わっているかもしれない。
 }
 // スコープを抜けたので参照カウントがデクリメントされる。
```

#### _retn()

現在持っているオブジェクト参照の所有権を放棄してポインタを返します。

```
 T_ptr _retn()
 {
	T_ptr tmp = pd_objref;
	pd_objref = T_Helper::_nil();
	return tmp;
 }
```

通常、関数の戻り値にオブジェクト参照を返す場合に使用されます。
所有権は関数の呼び出し側に渡るので、呼び出し側ではオブジェクト参照を破棄する必要があります。
従って、呼び出し側で release するか、_var型変数で受ける必要があります。

逆に、戻り値でオブジェクト参照を返す場合、呼び出し側で release することにより参照カウントがデクリメントされるため、関数内では _duplicate() などで所有権を複製しておく必要があります。

- 使用例

```
 MyObject_ptr myfunc()
 {
	MyObject_var ret;
	ret = m_obj; // ×所有権がretに移ってしまう。
	// return 後、関数の外で release されるかもしれない。
 
	ret = MyObject::_duplicate(m_obj); // ○所有権の複製
	// return 後、release が呼ばれても、m_obj は所有権を保持し続ける。
 
	return ret._retn();
 }
 
 { // 別のコンテキスト

	MyObject_var obj;
	obj = myfunc(); // オブジェクトの所有権を取得
	obj->function();
 
	MyObject_ptr ptr;
	ptr = myfunc(); //オブジェクトの所有権を取得
	ptr->function();
 
	CORBA::release(ptr); // 参照カウントをデクリメント
 
  }
  // スコープを抜けたので参照カウントがデクリメントされる
```


#### 規則のまとめ

<table class="table-alt">
  <tr>
    <th>関数</th>
    <th>型</th>
    <th>release責任</th>
    <th>関数内</th>
  </tr>
  <tr>
    <td>in</td>
    <td>T_ptr</td>
    <td>呼出側</td>
    <td>オペレーション呼出</td>
  </tr>
  <tr>
    <td>out</td>
    <td>T_ptr&</td>
    <td>呼出側</td>
    <td>&#95;duplicate 代入</td>
  </tr>
  <tr>
    <td>inout</td>
    <td>T_ptr&</td>
    <td>in:関数, out:呼出側</td>
    <td>release後, &#95;duplicate代入</td>
  </tr>
  <tr>
    <td>&#95;retn</td>
    <td>T_ptr</td>
    <td>呼出側</td>
    <td>&#95;duplicateしてreturn</td>
  </tr>
</table>

### _var型、_ptr型の代入でのリファレンスカウント
#### _ptr型への_var型の代入

ポインタへの代入。

複製なし、解放せず。

- 使用例

```
 { 
	MyObject_var var;
	var = myfunc(); // オブジェクトの所有権を取得
 
	MyObject_ptr ptr
	ptr = MyObject::_duplicate(var); //オブジェクトの所有権を取得(参照カウントのインクリメント)
 
	// ptr = var;
	// これは参照カウントエラーを引き起こす恐れがある。呼び出し後、ptrとvarは同じオブジェクト
	// をさすであろうが、参照カウントの保守はなされな。varは、その対象オブジェクトの所持を維持
	// する。また、ptrがそれが以前に指していたオブジェクトやプロキシへの唯一のポインタであった
	// とすれば、メモリリークが生じる。
 
	CORBA::release(ptr); // 参照カウントをデクリメント
 }
 // var に関しては、スコープを抜けたので参照カウントがデクリメントされる
```

#### _var型への_ptr型の代入

_var が保有しているオブジェクトに対して release() されるが、引数で渡された _ptr型のオブジェクトに対しては duplicate() されません。


複製なし、解放あり。

- 実装(omniORB)

```
  inline T_var& operator= (T_ptr p)
 {
	T_Helper::release(pd_objref);
	pd_objref = p;
	return *this;
  }
```

- 使用例

```
 { 
	MyObject_ptr ptr;
	ptr = myfunc(); // オブジェクトの所有権を取得
 
	MyObject_var obj;
	obj = MyObject::_duplicate(ptr); //オブジェクトの所有権を取得(参照カウントのインクリメント)
 
	CORBA::release(ptr); // 参照カウントをデクリメント
 
 }
 // objに関しては、スコープを抜けたので参照カウントがデクリメントされる
```

#### _var型への_var型の代入

_var が保有しているオブジェクトに対して release() がコールされ、
かつ、引数で渡されたオブジェクトに対しても duplicate() がコールされる。


複製あり、解放あり。


- 実装(omniORB)

```
  inline T_var& operator= (const T_var& p)
 {
	if( &p != this )
	{
		T_Helper::duplicate(p.pd_objref);
		T_Helper::release(pd_objref);
		pd_objref = p.pd_objref;
 	}
	return *this;
  }
```

- 使用例

```
 { 
	MyObject_var var1;
	var1 = myfunc(); // オブジェクトの所有権を取得
 
	MyObject_var var2;
	var2 = var1; //オブジェクトの所有権を取得(参照カウントは自動でインクリメントされる)

	} // var1, var2に関しては、スコープを抜けたので参照カウントがデクリメントされる
```

### _narrow()でのリファレンスカウント

_narrow()処理の過程において、_narrow()の呼び出しが成功した場合、その対象オブジェクトのリファレンスカウントはインクリメントされますが、失敗した場合はインクリメントされません。

デクリメントは行われない。

- 実装(RTCSK.cc)

```
 RTC::RTObject_ptr
 RTC::RTObject::_narrow(::CORBA::Object_ptr obj)
 {
	if( !obj || obj->_NP_is_nil() || obj->_NP_is_pseudo() ) return _nil();
	_ptr_type e = (_ptr_type) obj->_PR_getobj()->_realNarrow(_PD_repoId);
	return e ? e : _nil();
 }
```

- 実装(omniObjRef.cc)

```
 void*
 omniObjRef::_realNarrow(const char* repoId)
 {
	// Attempt to narrow the reference using static type info.
	void* target = _ptrToObjRef(repoId);
 
	if( target )
	{
		if (!lid ||
			(lid && !lid->deactivated() && lid->servant() &&
	 		lid->servant()->_ptrToInterface(repoId)))
		{
 		      omni::duplicateObjRef(this);
    		}
   		else
		{
      			omniObjRef* objref;
      			omniIOR*    ior;

			ior = pd_ior->duplicateNoLock();
      		}
 
		objref = omni::createObjRef(repoId,ior,1,0);
	}
	else
	{

    		if( _real_is_a(repoId) )
		{
			omniObjRef* objref;
			omniIOR* ior;
			{
				ior = pd_ior->duplicateNoLock();
			}
			{
				objref = omni::createObjRef(repoId,ior,1,_identity());
			}
 		}
 	 }
	return target;
 }
```

### 規則 

#### クライアント側

クライアントが呼び出しからオブジェクト参照を受信するならば、そのクライアントはそのオブジェクト参照が不要となったときにはそれを開放しなくてはならない。

(引用：　『CORBA分散オブジェクト　Orbixを用いて』　P.98 オブジェクト参照のためのメモリ管理)

#### サーバー側 

呼び出し側に渡す参照の所有権は放棄される(つまり、その参照カウントは一つデクリメントされる。したがって、通常は、参照を返す前に適当な_duplicate()関数を呼び出すことになる)

(引用：　『CORBA分散オブジェクト　Orbixを用いて』　P.98 オブジェクト参照のためのメモリ管理)

#### 参考文献
- 『CORBA分散オブジェクト　Orbixを用いて』　著: ショーン・ベーカー　出版社: ピアソン・エデュケーション


## サービスコンシューマからサービスプロバイダの状態を取得する

コンシューマからプロバイダを呼び出す際には、サービスポートが接続されていて、かつ相手の RTC が Active 状態になっている必要があります。コンシューマは、コンシューマが接続されているか、相手の RTC がアクティブかどうかを以下の方法で確認することができます。

CORBA コンシューマ型 (C++ では RTC::CorbaComsumer<T>) は以下の3つの状態を取ることができます。

<!-- You can also know the state of an RTC through service ports if -->
<!-- the RTC has provided interfaces (provider) on it. -->
<!-- RTC::CorbaComsumer<> can be three states: nil, inactive, active. -->

- **nil**: コンシューマにプロバイダのオブジェクト参照がセットされていない(接続されていない)状態
- **active**: プロバイダのオブジェクト参照は割り当てられており、かつ相手のオブジェクトが活性化 (RTC も Active 状態) になっている状態
- **inactive**: プロバイダのオブジェクト参照は割り当てられているが、相手のオブジェクトが非活性化 (RTC は Inactive 状態) になっている状態

プロバイダの状態と RTC の状態は連動しています。
- 参照: [cxx/classreference_en/classRTC_1_1CorbaPort](https://www.openrtm.org/OpenRTM-aist/documents/current/cxx/classreference_en/classRTC_1_1CorbaPort.html#a1b9efe804a293b2c38a9cbe3b5ba54a0)

RTC::CorbaComsumer<T> が nil かどうかは、CORBA の標準関数：CORBA::is_nil() で確認することができます。
さらに、オブジェクトがアクティブかどうかは、CORBA オブジェクトのメンバ関数、_non_existent() で確認することができます。

こういった情報は CORBA のマニュアルやドキュメントから得ることができます。一番確実なのは OMG から入手できる CORBA の仕様書を読むことです。

- [CORBA 仕様書一覧](http://www.omg.org/spec/CORBA)
- [CORBA インターフェース仕様書(v3.3)](http://www.omg.org/spec/CORBA/3.3/Interfaces/PDF)

しかしながら、これらの標準仕様書はページ数も多いので、例えば VisiBroker などの CORBA 製品のマニュアルを利用するとよいかもしれません。

以上の情報から以下のようなサンプルコードが書けます。

```
 RTC::ReturnCode_t MyServiceConsumer::onExecute(RTC::UniqueId ec_id)
 {
   try
     {
       if (CORBA::is_nil(m_myservice0._ptr()))
         {
           std::cout << "[nil] object reference is not assigned." << std::endl;
         }
       else
         {
           if (m_myservice0->_non_existent())
             {
               std::cout << "[inactive] provider is inactive." << std::endl;
             }
           else
             {
               std::cout << "[active] provider is active." << std::endl;
             }
         }
     }
   catch (...)
     {
       std::cout << "Unknown exception." << std::endl;
     }
   coil::sleep(1);
   return RTC::RTC_OK;
 }
```

このコードの onExecute 関数を OpenRTM-aist のサンプル SimpleService の MyServiceConsumer.cpp の oExecute 関数と入れ替えて MyServiceProviderComp とともに実行してみてください。
MyServiceConsumerComp をアクティブ化すると、MyServiceProviderComp のサービスポートが接続されるまではコンシューマ (m_myserivce0) の状態は nil です。MyServiceProviderComp のポートを接続すると、inactive 状態になり、その後 MyServiceProvider をアクティブ化すると active 状態になります。

以上のようにして、相手の RTC の状態をサービスポートを通して知ることもできます。

## 独自IDLファイルの利用

### RTC Builderでプロジェクト作成

RTCBuilder でプロジェクトの作成を行います。

「RTC Builder Project」のアイコンをクリックし、表示したウィンドウにプロジェクト名を入力し「終了」すると、左のウィンドウに生成したプロジェクトファイルが表示します。
<div align="center"><a href="sp_idl_0.png"><img src="sp_idl_0.png" width="80%;"></a></div>
<div align="center">「RTC Builder Project」ウィンドウを表示</div>

<div align="center"><a href="sp_idl_00.png"><img src="sp_idl_00.png" width="50%;"></a></div>
<div align="center">idlフォルダーの確認</div>

そこに独自データ型を配置するidlフォルダーがあるので、idlファイルをドラッグ&ドロップや[右クリック]>[貼り付け]などで置いてください。

ここではサンプルコンポーネントのSampleServiceコンポーネントが使用するIDLファイル（MyService.idl）を使います。
IDLファイル（MyService.idl）の保存先は以下です。
- Windows環境でパッケージをインストールした場合は[インストールディレクトリ\OpenRTM-aist\1.2.2\Components\Python\Examples\SimpleService\MyService.idl]です。
<!-- -- ソースコードの場合は[./examples/SimpleService/MyService.idl]にあります。 -->

プロジェクトフォルダーは、RTCBuilder起動直後に表示する「ディレクトリをワークスペースとして選択」をデフォルトで進めた場合、[ c:\Users\ユーザ名\workspase ]フォルダー以下にあります。

### 独自IDLの作成

RTCBuilder で独自idlを使ったコンポーネントの作成を行います。


サービスポート設定タブを開き、[Add Port]を選択しサービスポート（ServicePort）を定義します。

[ Add Interface ] ボタンを２回クリックし[ Service Interface ] を表示・選択すると[ Service Interface Profile ]を表示します。

<div align="center"><a href="sp_idl_01_0.png"><img src="sp_idl_01_0.png" width="80%;"></a></div>
<div align="center">独自インターフェースを使う</div>

[Reload] をクリックするとidlフォルダー内のidlファイルが読み込まれ、 ***インターフェース型** のプルダウンで新たに定義した独自インターフェースを選択できます。

その他、コンポーネント作成に必要な項目の設定が終わったら、基本タブに戻り、[コード生成] ボタンをクリックし、コードの生成を行います。


