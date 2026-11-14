---
layout: page
title: 変数受渡規則
---

<!-- Title: 変数受渡規則 -->
#contents
#clear
## 構造体・/オブジェクトリファレンス 

CORBA の構造体は C++ において、構造体 "struct" にマッピングされる。
```
 // -*- IDL -*-
 struct Profile {
   short short_value;
   long  long_value;
 };
```

```
 // -*- C++ -*-
 struct Profile {
   CORBA::Short short_value;
   CORBA::Long  long_value;
 };
```

```
 class Profile_var {
   
 };
```

- 固定長の構造体


- 可変長の構造体

構造体に可変長のメンバー (string、wstring、sequence (可変長メンバを持つ struct、可変長メンバを持つ union) が含まれていると、構造体は可変長データとみなされます。
この場合、固定長の構造体とは異なる C++ コードが生成され、戻り値や outパラメータにおける扱いが異なります。

  - _var型
IDL コンパイラは IDL における構造体から、C++ の構造体と _var 型のクラスを自動的に生成します。
_var 型クラスはスマートポインタのように振る舞い、可変長の構造体として _var クラスを使用する場合、可変長のメンバーに割り当てられるメモリーは自動的に管理されます。 

  - _var 型の変数(例えば var1)から他の_var型の変数(var2)に代入が行われた場合には、そのポインタの所有権が var2 に移り、その後 var1 は初期化もしくは代入が行われるまで、使用することはできません。
  - 構造体がスコープの外に出ると，可変長のメンバーに関連付けられていたすべてのメモリは自動的に解放されます。 ただし、すでに所有権を他に譲渡している_var型変数がスコープから出る場合、元のデータに対しては開放は行われません。(所有権を既に譲渡しているので。)
  - 初期化もしくは代入された構造体に対して，再び初期化または代入が行われた場合，元のデータに関連付けられていたメモリは自動的に解放されます。
  - 可変長のメンバーにオブジェクトリファレンスが代入される場合は，必ずそのオブジェクトリファレンスのコピーが作成されます。可変長のメンバーにポインタが代入される場合，コピーは作成されません。



### _var 型
#### 変換コンストラクタ(T_ptr)

- 実装例
```
  _CORBA_ObjRef_Var(T_ptr p) : pd_objref(p) {}
```

_ptr型のオブジェクト参照の所有権は_var型に移るため、参照カウントの増減はない。

```
 MyObject_ptr ptr = obj->get_myobject();
 // ptr は適切なタイミングでreleaseされなければならない
 MyObject_var var(ptr);
 // 所有権は var に移ったため、ptr をリリースする必要はない
 // var がスコープを抜けるなどして解体されるとき参照カウントはデクリメントされる
 
```
#### 変換コンストラクタ(const T_var&)
- 実装例
```
 Object_var(const T_var& p) : pd_ref(T::_duplicate(p.pd_ref)) {}
```

代入元の_var型のオブジェクト参照の所有権はコピーされる。

```
 MyObject_var var0 = obj->get_myobject();
 // var0 は所有権をもつ
 MyObject_var var1(var0);
 // リファレンスカウントはインクリメントされ var1も所有権を持つ
```

#### 変換コンストラクタ(const T_member) 
- 実装例

#### in引数とin()関数
単純にオブジェクト参照の_ptr型ポインタを返す。
所有権の移動は起こらない。

- 実装例
```
 T_ptr  in() const { return pd_objref; }
```

通常、関数の**in**引数にオブジェクト参照を渡す際に使用する。
オブジェクト参照を与えられた側の関数は、所有権を持たないため関数内で**release**してはいけない。
関数から戻ってきたあと、_var型変数に依然として所有権が保持されており、_var型変数の解体時にオブジェクトは**release**される。

オブジェクト参照を**in**引数として受け取る関数を定義する場合は、_ptr型の引数として定義する。さらに、関数内では、そのオブジェクトのオペレーションを呼ぶだけで、**release**等は行ってはいけない。
また、関数内でオブジェクト参照をどこか(グローバル変数、static 変数、オブジェクトのメンバー等)に保存したい場合は、所有権をコピーするため duplicate関数で複製する必要がある。


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
   myfunc(obj.in()); // 所有権の移行は起こらない
 }
 // スコープを抜けたので参照カウントがデクリメントされる
```

#### out引数と out()関数 
現在所有している参照を**release**(参照カウントをデクリメント)して、リファレンスのポインタをnilにセットして返す。
すなわち、**out()**関数呼び出し以前にもしオブジェクト参照を保持している場合はその所有権を放棄し参照は破棄される。

- 実装例

```
 T_ptr& out() {
    T_Helper::release(pd_objref);
    pd_objref = T_Helper::_nil();
    return pd_objref;
 }
```

通常、関数の**out**引数にオブジェクト参照を渡す際に使用する。すなわち、関数から戻ってきたあと、この変数に新たにオブジェクト参照が保持されていることが期待される。
このとき、オブジェクト参照の所有権はこの変数に保持されていると考える。
**out()**で変数を渡された関数側では、何らかの形でオブジェクト参照を生成または複製して、引数に所有権を渡す必要がある。

オブジェクト参照を**out**引数として受け取る関数を定義する場合は、_ptr型参照の引数として定義する。関数内では、引数は必ずnilオブジェクト参照であり、かつ通常何らかのオブジェクトを所有権を与えて代入することが期待される。

- 使用例

```
 void myfunc(MyObject_ptr& obj)
 {
   assert(CORBA::is_nil(obj)); // 必ずnilオブジェクト
   obj->function(); // nilなのでオペレーションは呼べない
 
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
リファレンスへのポインタの参照を返す。

- 実装

```
 T_ptr& inout()    { return pd_objref; }
```

通常、関数の**inout**引数にオブジェクト参照を渡す際に使用する。
すなわち、関数内では何らかのオブジェクト参照が引数に入っていることが期待され、オブジェクトの所有権は関数側に移る。また、関数は何らかのオブジェクト参照をこの引数に与えて返すことが期待され、引数すなわち呼び出し元の変数に所有権を与える。
関数内では引数にオブジェクト参照を新たにセットする場合は、まず**release**してから新たなオブジェクト参照を生成または複製して引数に所有権を渡す必要がある。

オブジェクト参照を**inout**引数として取る関数は、設計の観点からあまり推奨されない。もし、**inout**引数として取る関数を定義する必要がある場合は、_ptr型参照の引数として定義する。

- 使用例

```
 void myfunc(MyObject_ptr& obj)
 {
   if (!CORBA::is_nil(obj))
   {
     obj->function(); // obj がnilでなければオペレーションを呼ぶことができる。
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
   // return 後、関数の外でreleaseされるかもしれない。
   obj = MyObject::_duplicate(m_obj); // ○ obj にもMyObjectの所有権が与えられた
   // return 後、関数の外でreleaseされても、オブジェクト参照は解体されない。
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
現在持っているオブジェクト参照の所有権を放棄してポインタを返す。

```
 T_ptr _retn() {
    T_ptr tmp = pd_objref;
    pd_objref = T_Helper::_nil();
    return tmp;
 }
```

通常、関数の戻り値にオブジェクト参照を返す場合に使用される。
所有権は関数の呼び出し側に渡るので、呼び出し側ではオブジェクト参照を破棄する責任がある。したがって、呼び出し側で release するか、_var型変数で受ける必要がある。

逆に、戻り値でオブジェクト参照を返す場合、呼び出し側では必ず release により参照カウントがデクリメントされるため、関数内では_duplicate()などで所有権を複製しておく必要がある。

- 使用例

```
 MyObject_ptr myfunc()
 {
   MyObject_var ret;
   ret = m_obj; // ×所有権がretに移ってしまう。
   // return 後、関数の外でreleaseされるかもしれない。
 
   ret = MyObject::_duplicate(m_obj); // ○所有権の複製
   // return 後、releaseが呼ばれても、m_obj は所有権を保持し続ける。
 
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
    <td>T_ptr&amp;</td>
    <td>呼出側</td>
    <td>_duplicate 代入</td>
  </tr>
  <tr>
    <td>inout</td>
    <td>T_ptr&</td>
    <td>in:関数, out:呼出側</td>
    <td>release後, _duplicate代入</td>
  </tr>
  <tr>
    <td>_retn</td>
    <td>T_ptr</td>
    <td>呼出側</td>
    <td>_duplicateしてreturn</td>
  </tr>
</table>

### _var型,_ptr型の代入でのリファレンスカウント
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

_var が保有しているオブジェクトに対して release() されるが、
引数で渡された _ptr型のオブジェクトに対しては duplicate() されない。


複製なし、解放あり。

- 実装(omniORB)

```
  inline T_var& operator= (T_ptr p) {
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
  inline T_var& operator= (const T_var& p) {
    if( &p != this ) {
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

_narrow()処理の過程において、_narrow()の呼び出しが成功した場合、その対象オブジェクトのリファレンスカウントはインクリメントされるが、失敗した場合はインクリメントされない。

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
 
  if( target ) {
    if (!lid ||
	(lid && !lid->deactivated() && lid->servant() &&
	 lid->servant()->_ptrToInterface(repoId))) {
 
      omni::duplicateObjRef(this);
    }
    else {
      omniObjRef* objref;
      omniIOR*    ior;
 
      {
	ior = pd_ior->duplicateNoLock();
      }
 
      {
	objref = omni::createObjRef(repoId,ior,1,0);
      }
    }
  }
  else {
    if( _real_is_a(repoId) ) {
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

