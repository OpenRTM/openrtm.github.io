---
layout: page
title: rules for passing variables
---

<!-- Title: 変数受渡規則 -->
#contents
#clear
## Structures / Object References 

CORBA structures are mapped to the structure "struct" in C++.
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

- Fixed-length structures


- Variable-length structures

If a structure contains variable-length members (string, wstring, sequence, struct with variable-length members, or union with variable-length members), the structure is considered variable-length data.
In this case, C++ code different from that for fixed-length structures is generated, and handling differs for return values and out parameters.

  - _var type
The IDL compiler automatically generates a C++ structure and a _var type class from a structure in IDL.
The _var type class behaves like a smart pointer, and when using the _var class as a variable-length structure, the memory allocated to variable-length members is automatically managed. 

  - When assignment is performed from a _var type variable (for example, var1) to another _var type variable (var2), ownership of that pointer moves to var2, and after that, var1 cannot be used until it is initialized or assigned again.
  - When a structure goes out of scope, all memory associated with variable-length members is automatically released. However, when a _var type variable that has already transferred ownership to another variable goes out of scope, the original data is not released. (Because ownership has already been transferred.)
  - When a structure that has been initialized or assigned is initialized or assigned again, the memory associated with the original data is automatically released.
  - When an object reference is assigned to a variable-length member, a copy of that object reference is always created. When a pointer is assigned to a variable-length member, no copy is created.



### _var Type
#### Conversion Constructor (T_ptr)

- Implementation example
```
  _CORBA_ObjRef_Var(T_ptr p) : pd_objref(p) {}
```

Because ownership of the _ptr type object reference moves to the _var type, there is no increase or decrease in the reference count.

```
 MyObject_ptr ptr = obj->get_myobject();
 // ptr は適切なタイミングでreleaseされなければならない
 MyObject_var var(ptr);
 // 所有権は var に移ったため、ptr をリリースする必要はない
 // var がスコープを抜けるなどして解体されるとき参照カウントはデクリメントされる
 
```
#### Conversion Constructor (const T_var&)
- Implementation example
```
 Object_var(const T_var& p) : pd_ref(T::_duplicate(p.pd_ref)) {}
```

Ownership of the object reference of the source _var type is copied.

```
 MyObject_var var0 = obj->get_myobject();
 // var0 は所有権をもつ
 MyObject_var var1(var0);
 // リファレンスカウントはインクリメントされ var1も所有権を持つ
```

#### Conversion Constructor (const T_member) 
- Implementation example

#### in Argument and in() Function
Simply returns a _ptr type pointer to the object reference.
No ownership transfer occurs.

- Implementation example
```
 T_ptr  in() const { return pd_objref; }
```

Usually used when passing an object reference to an **in** argument of a function.
The function receiving the object reference does not have ownership, so it must not **release** it inside the function.
After returning from the function, ownership is still retained by the _var type variable, and the object is **released** when the _var type variable is destructed.

When defining a function that receives an object reference as an **in** argument, define it as a _ptr type argument. Furthermore, inside the function, only call operations on that object; do not perform **release** or similar operations.
Also, if you want to save the object reference somewhere inside the function (global variable, static variable, object member, etc.), you need to duplicate it using the duplicate function in order to copy ownership.


- Usage example

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

#### out Argument and out() Function 
Releases the currently owned reference (**release**, decrements the reference count), sets the reference pointer to nil, and returns it.
In other words, if an object reference is held before calling the **out()** function, its ownership is abandoned and the reference is destroyed.

- Implementation example

```
 T_ptr& out() {
    T_Helper::release(pd_objref);
    pd_objref = T_Helper::_nil();
    return pd_objref;
 }
```

Usually used when passing an object reference to an **out** argument of a function. In other words, after returning from the function, this variable is expected to hold a new object reference.
At this time, ownership of the object reference is considered to be held by this variable.
The function side that receives the variable with **out()** must create or duplicate an object reference in some form and pass ownership to the argument.

When defining a function that receives an object reference as an **out** argument, define it as a _ptr type reference argument. Inside the function, the argument is always a nil object reference, and normally it is expected that some object will be assigned with ownership.

- Usage example

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
Returns a reference to the pointer to the reference.

- Implementation

```
 T_ptr& inout()    { return pd_objref; }
```

Usually used when passing an object reference to an **inout** argument of a function.
In other words, inside the function, some object reference is expected to be contained in the argument, and ownership of the object moves to the function side. Also, the function is expected to provide some object reference to this argument and return it, giving ownership to the argument, that is, the caller's variable.
Inside the function, when setting a new object reference to the argument, it is necessary to first **release** it, then create or duplicate a new object reference and pass ownership to the argument.

Functions that take object references as **inout** arguments are not very recommended from a design standpoint. If it is necessary to define a function that takes an **inout** argument, define it as a _ptr type reference argument.

- Usage example

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
Abandons ownership of the currently held object reference and returns the pointer.

```
 T_ptr _retn() {
    T_ptr tmp = pd_objref;
    pd_objref = T_Helper::_nil();
    return tmp;
 }
```

Usually used when returning an object reference as the return value of a function.
Ownership is passed to the function caller, so the caller is responsible for destroying the object reference. Therefore, the caller must either release it or receive it with a _var type variable.

Conversely, when returning an object reference as a return value, the caller always decrements the reference count with release, so ownership must be duplicated inside the function using _duplicate() or similar.

- Usage example

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


#### Summary of Rules

<table class="table-alt">
  <tr>
    <th>Function</th>
    <th>Type</th>
    <th>release responsibility</th>
    <th>Inside the function</th>
  </tr>
  <tr>
    <td>in</td>
    <td>T_ptr</td>
    <td>Caller</td>
    <td>Operation call</td>
  </tr>
  <tr>
    <td>out</td>
    <td>T_ptr&amp;</td>
    <td>Caller</td>
    <td>_duplicate assignment</td>
  </tr>
  <tr>
    <td>inout</td>
    <td>T_ptr&</td>
    <td>in: function, out: caller</td>
    <td>After release, _duplicate assignment</td>
  </tr>
  <tr>
    <td>_retn</td>
    <td>T_ptr</td>
    <td>Caller</td>
    <td>_duplicate and return</td>
  </tr>
</table>

### Reference Counts in Assignment of _var Type and _ptr Type
#### Assignment of _var Type to _ptr Type

Assignment to a pointer.

No duplication, no release.

- Usage example

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

#### Assignment of _ptr Type to _var Type

release() is performed on the object held by _var,
but duplicate() is not performed on the _ptr type object passed as the argument.


No duplication, with release.

- Implementation (omniORB)

```
  inline T_var& operator= (T_ptr p) {
    T_Helper::release(pd_objref);
    pd_objref = p;
    return *this;
  }
```

- Usage example

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

#### Assignment of _var Type to _var Type

release() is called on the object held by _var,
and duplicate() is also called on the object passed as the argument.


With duplication, with release.


- Implementation (omniORB)

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

- Usage example

```
 { 
  MyObject_var var1;
  var1 = myfunc(); // オブジェクトの所有権を取得
 
  MyObject_var var2;
  var2 = var1; //オブジェクトの所有権を取得(参照カウントは自動でインクリメントされる)
 
  } // var1, var2に関しては、スコープを抜けたので参照カウントがデクリメントされる
```

### Reference Counts in _narrow()

In the process of _narrow(), if the _narrow() call succeeds, the reference count of the target object is incremented; if it fails, it is not incremented.

No decrement is performed.

- Implementation (RTCSK.cc)

```
 RTC::RTObject_ptr
 RTC::RTObject::_narrow(::CORBA::Object_ptr obj)
 {
   if( !obj || obj->_NP_is_nil() || obj->_NP_is_pseudo() ) return _nil();
   _ptr_type e = (_ptr_type) obj->_PR_getobj()->_realNarrow(_PD_repoId);
   return e ? e : _nil();
 }
```

- Implementation (omniObjRef.cc)

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

### Rules 

#### Client Side

If a client receives an object reference from an invocation, that client must release the object reference when it is no longer needed.

(Quote: "CORBA Distributed Objects Using Orbix," p.98, Memory Management for Object References)

#### Server Side 

Ownership of the reference passed to the caller is abandoned (that is, its reference count is decremented by one. Therefore, normally, an appropriate _duplicate() function is called before returning the reference.)

(Quote: "CORBA Distributed Objects Using Orbix," p.98, Memory Management for Object References)

#### References
- "CORBA Distributed Objects Using Orbix" Author: Sean Baker Publisher: Pearson Education

