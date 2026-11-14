---
layout: page
title: _var_type, _ptr_type
---

<!-- Title: _var_type, _ptr_type -->
#contents
## _ptr_type、_var_type について
template class を作成するときに、オブジェクトの型と、_ptr型、_var型がそれぞれ必要になる場合があります。

```
 interface Hello {
    void hello_world();
 };
```

といったインターフェースが定義されている場合、クライアント側では、Hello、Hello_ptr、Hello_var を使用することになりますが、_ptr、_var 型は単なる Hello のポインタではありませんので、これらを全て使うテンプレートクラスの宣言などは、

```
 template <class Hello, class Hello_ptr, class Hello_var)
 class HelloHelper
 {
   :
 } 
```

等のように書く必要があります。
しかし、実際には、omniORB などでは Hello クラス内で　_ptr型、_var型をそれぞれ、_ptr_type、_var_type に typedef して利用しています。
omniORB で生成したスタブのコードの一部、

```
 typedef _objref_hello* hello_ptr; // _ptr は objref_hello* への typedef
 typedef _CORBA_ObjRef_Var<_objref_hello, hello_Helper> hello_var; // _var型
 class hello {
 public:
   // Declarations for this interface type.
   typedef hello_ptr _ptr_type; // hello_ptr は typename hello::_ptr_type
   typedef hello_var _var_type; // hello_var は typename hello::_var_type
```

このように定義されています。
従って、上記の template は以下のように書くことができます。

```
 template<class ObjectType,
          class ObjectTypePtr = typename ObjectType::_ptr_type,
          class ObjectTypeVar = typename ObjectType::_var_type>
 class HogeHelper
 {
    :
 } 
```


ただし、CORBA の仕様を見る限りでは _ptr_type や _var_type が標準として定められているわけではなさそうですので、この方法はポータブルな方法ではありません。
少なくとも omniORB4 でのみは確実に動作しそうですが、ほかの実装では、どのように定義されているかわかりません。
（定義が異なる場合は、template の第2引数、第3引数にそれぞれ_ptr型や、_var型を与えれば使えますが。。。）

## 他の ORB での定義の仕方
### omniORB4
上記のように、_ptr_type、_var_type が使えます。

### TAO
TAO でも、同様の方法が使えます。
以下は、TAOのスタブの一部抜粋。

```
 class  Hello
    : public virtual CORBA::Object
  {
  public:
    friend class TAO::Narrow_Utils<Hello>;
    typedef Hello_ptr _ptr_type;
    typedef Hello_var _var_type;
```


### MICO
MICO も同様に _ptr_type、_var_type が typedef されているので、同様の方法が使えます。
ただし、HAVE_TYPEDEF_OVERLOAD が define されている必要があるようですが、デフォルトでは _ptr_type、_var_type にアクセスできるようなので、問題ないようです。

```
 class Hello : 
   virtual public CORBA::Object
 {
   public:
     virtual ~Hello();
     #ifdef HAVE_TYPEDEF_OVERLOAD
     typedef Hello_ptr _ptr_type;
     typedef Hello_var _var_type;
     #endif
```


### ORBacus 
手元に開発環境が無いため、google CodeSearch で探したところ、このようなコードがありましたので、状況は同じものと思われます。

```
 class Codec : virtual public CORBA::Object
 {
     Codec(const Codec&);
 public:
     Codec() { }
     typedef Codec_ptr _ptr_type;
     typedef Codec_var _var_type;
```



### ORBit2 

google CodeSearch で、このようなコードを見つけました。
CosNaming の BindingIterator のスタブだと思われますが、_ptr_type、_var_type が定義されています。

```
 class BindingIterator : public virtual CORBA::Object
 {
 public:
   typedef ::CosNaming::BindingIterator_ptr _ptr_type;
   typedef ::CosNaming::BindingIterator_var _var_type;
```
