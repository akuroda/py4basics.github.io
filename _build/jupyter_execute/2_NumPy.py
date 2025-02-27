#!/usr/bin/env python
# coding: utf-8

# (chap:numpy)=
# # `NumPy`：高速化

# `NumPy`は，数値計算をする上で重要な役割を果たすパッケージであり，特に，行列計算に威力を発揮する。`NumPy`は「ナンパイ」と読む。慣例として`np`としてインポートする。

# In[1]:


import numpy as np


# ## `array`

# 基本となる関数が`np.array()`であり，次のコードでは１次元配列を作る。

# In[2]:


arr = np.array([10, 20, 30, 40, 50])
arr


# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Start
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/><input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="translation" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# 次に２次元配列を作成しよう。

# In[3]:


mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
mat


# `mat`は行列と解釈できる。データ型を確認してみよう。

# In[4]:


print(type(arr))
print(type(mat))


# `arr`と`mat`は`NumPy`の`ndarray`（`n`次元`array`）というデータ型（クラス）である。`[]`に囲まれた数字が並んでいてリストと似ているように感じるかも知れないが、処理速度が格段に早く、より簡単なコードで同じ処理ができるなど使い勝手が大きく向上することが`NumPy`の大きな特徴となる。科学計算やデータ処理では欠かせないパッケージとなっている。
# 
# 次のコードが示すように、リストから`ndarray`を作成することができる

# In[5]:


l = [1,2,3,4,5]

np.array(l)


# In[6]:


np.array([l,l])


# 後述するが、`ndarray`をリストに変換するメソッドも用意されている。
# 
# `array`について[このサイト](https://note.com/sayajewels/n/n95edaedb0fc5)では図を使って説明しているので興味があるひとは参考にしてはどうだろうか。

# ## １次元配列

# ### 要素の抽出

# リストと同じように`arr`の要素を抽出するには要素のインデックスを使う。

# In[7]:


arr[1]


# 複数の要素を抽出するにはインデックスをリストとして使う。

# In[8]:


arr[[0,1,3]]


# 要素を連続で抽出するスライシング（slicing）も使うことができる。

# In[9]:


arr[1:3+1]


# リストの場合と同じ様に，`:`の左側が選択する最初の要素であり，`:`の右側が選択する最後の次の番号である（即ち，`:`の右側の番号の要素は含まれない。

# ### 要素の代入と削除

# 要素の入れ替え方法を説明するために，上で作成したリスト`arr`を考えてみよう。

# In[10]:


arr


# `30`を`3000`に入れ替えてみよう。リストや辞書と同じように`=`を使い値を代入する。

# In[11]:


arr[2] = 3000
arr


# 要素を削除するには関数`np.delete()`を使う。第一引数に`array`を，第二引数に削除したい要素のインデックスを指定する。例えば，`3000`を削除したいとしよう。

# In[12]:


np.delete(arr,2)


# ここでもう一度`arr`を表示してみよう。

# In[13]:


arr


# `3000`は残ったままである。`np.delete()`を実行すると，もし`3000`を削除するとどうなるかを示している。`arr`自体を変更したい場合は`=`を使って再割り当てをする必要がある。

# In[14]:


arr = np.delete(arr,2)
arr


# これは`np.delete()`特有なものではなく，他の関数（例えば，`np.log()`や`np.sqrt()`）も同じである。

# ## ２次元配列：要素の抽出

# 第$i$行目の第$j$列目要素にアクセスするためには`mat[i,j]`と書く。`[,]`の`,`を挟んで左が行を表し，右が列を示す。
# ```
# [行のインデックス,列のインデックス]
# ```
# 
# コードはキーストロークが少なく，簡単なものが良いと考えられている。一方で，`Python`は初心者に比較的簡単な言語だと言われるが，それでも関数・メソッドの数は膨大で，そのオプションとの組み合わせを考えるとまさしく「無数」にあると言っても過言ではない。そのため初心者にとって関数の使い方やオプションの書き方を間違う可能性は小さくない。さらに，自分が書いたコードを数週間・数ヶ月後に読み直すと，何をしようとしているのか分からないという状況が生じることもある。従って，以下の点が非常に重要になる。
# 
# * 間違いにくいコードの書き方を覚える。
# * 高い可読性を意識したコードの書き方を覚える。
# 
# このスタンスに基づいて以下のルールに従って説明する。
# 
# 1. `[,]`内の`,`を省略可能な場合であっても省略しない。
# 2. `[,]`内の`,`の左または右を省略できる場合であっても省略しない。
# 
# 行または列を連続選択する（slicing）場合を考えよう。上でも説明したように`:`を使うが
# ```
# start:end
# ```
# となる。ここで`start`とは選択する要素の最初インデックスであり，`end`は選択する最後の要素の次のインデックスである（リストの場合と同じ）。このルールに従うと，
# 
# * `:`の左を省略すると「最初から」という意味になる。
# * `:`の右を省略すると「最後まで」という意味になる。
# * `,`の左または右が`:`のみの場合，「全て」という意味になる。
# 
# これを読むだけでは分かりにくいと思うので，以下の例に目を通してもう一度この箇所の説明を読んむことを推奨する。

# In[15]:


mat[0,1]


# 第$i$行の抽出は`mat[i,:]`で可能である。`:`は「列の全て」という意味になる。

# In[16]:


r0 = mat[0,:]
r0


# 抽出した行は上で説明した１次元配列なのでインデックスやスライシングを使って要素にアクセスすることができる。

# 複数の行の抽出は次の方法で可能である。

# In[17]:


mat[1:3,:]


# 第３行目は含まれないことに注意しよう。リストの要素の取り出し方と同じように`:`の右のインデックスの行は含まれない。
# 
# **（注意）**
# 
# `,:`を省略して`mat[1:3]`と書いてもエラーは発生せず同じ結果が返されるが，`,:`があることにより，行を抽出しており列は全て選択されていることが明示的になる。
# 
# 
# 第$i$ 列目を抽出したい場合は次のコードになる。

# In[18]:


mat[:, 1]


# 複数列の抽出は以下のようにする。

# In[19]:


mat[:, 1:3]


# ## `array`を使った計算

# まず２つの行列（２次元配列`array`）を作成する。

# In[20]:


m1 = np.array([[1, 1], [1, 1]])
m1


# In[21]:


m2 = np.array([[2, 2], [2, 2]])
m2


# これらは数学で習った行列のように見えるが，少し異なる性質（特に積）を持っているので注意しよう。

# ### 加算

# 要素ごとの和となる。

# In[22]:


m2 + m1


# ### 減算

# 要素ごとの差となる。

# In[23]:


m2 - m1


# ### スカラー乗算

# 与えられた定数とそれぞれの要素の積となる。

# In[24]:


10 * m1


# In[25]:


m1/2  # 1/2をかけるのと同じ


# ### 乗算：バージョン１

# `*`を使うと要素どうしの積となる。数学で学んだ行列の計算とは異なるので注意すること。

# In[26]:


m1*m2


# ### 乗算：バージョン２

# `@`を使うと数学で学んだ行列の積となる。

# In[27]:


m1@m2


# `numpy`の関数`dot()`は`@`と同じとなる。

# In[28]:


np.dot(m1,m2)


# ### 転置

# 数学で学ぶ転置行列と同じ。`m3`を使って説明する。

# In[29]:


m3 = np.array([[1,2,3],[4,5,6]])
m3


# `m3`のメソッド`transpose()`を使う。

# In[30]:


m3.transpose()


# `.transpose()`の省略形として`.T`を使うこともできる。

# In[31]:


m3.T


# ## `linalg`サブパッケージ

# ２次元配列の`array`は行列として使える。その特徴を活かして`NumPy`のサブパッケージである`linalg`（linear algebraの略であり「線形代数」という意味）を使うと連立方程式を解いたり固有値を簡単に計算することができる。

# ### 連立一次方程式の解

# (sec:2-simultaneousEq)=
# ### 連立一次方程式の解

# 連立一次方程式は行列表記できる。例えば，
# 
# $$
# \begin{align*}
#     a_{11}y + a_{12}x &= b_1\\
#     a_{21}y + a_{22}x &= b_2   
# \end{align*}
# $$
# 
# $$
# \Downarrow
# $$
# 
# $$
# a\cdot z=b
# $$

# ここで
# 
# $$
# a=
# \begin{bmatrix}
#     a_{11} & a_{12} \\
#     a_{21} & a_{22}
# \end{bmatrix}
# ,\quad
# z=
# \begin{bmatrix}
#     y \\
#     x
# \end{bmatrix}
# ,\quad
# b=
# \begin{bmatrix}
#     b_1 \\
#     b_2
# \end{bmatrix}
# $$
# 
# 
# 
# 解は逆行列を使い計算できる。
# 
# $$
# z=a^{-1}b
# $$

# #### `solve`

# `z`を求めるために`NumPy`のサブパッケージ`linalg`の中にある`solve`関数を使うが，次のような書き方となる。
# ```
# np.linalg.solve(a,b)
# ```
# このコードは`.`を助詞「の」として，`()`を「実行する」と読むと，次のように日本語として読むことができる。「`NumPy`の`linalg`の`solve`関数を引数`a`と`b`を使い実行する」と読める。では実際に`solve`を使って解を求めよう。

# In[32]:


a = np.array([[1,2],
              [3,4]])
b = np.array([20,10])


# In[33]:


sol = np.linalg.solve(a,b)


# ここで`sol`は解からなる`array`である。

# In[34]:


sol


# 分かりやすく次のように表示しよう。

# In[35]:


print(f'y = {sol[0]}\nx = {sol[1]}')


# #### `inv`

# `array`の逆行列は，サブパッケージ`linalg`の中にある`inv`で計算できる。`a`を例にとると，書き方は次のようになる
# ```
# np.linalg.inv(a)
# ```
# `solve`と同じように日本語として読むことができる。
# 
# では`a`の逆行列を計算して解を求めてみよう。

# In[36]:


a = np.array([[1,2],[3,4]])
a_inv = np.linalg.inv(a)
b = np.array([20,10])
a_inv@b


# 当たり前だが，同じ解である。

# ### 固有値：`eigvals`

# 行列の固有値を計算する`eigvals()`関数を紹介する。`a`を例に使うと次の書き方となる。
# ```
# np.linalg.eigvals(a)
# ```
# この関数は動学モデルの安定性（収束、発散）を調べる場合に役に立つ。より具体的な説明は後程おこなうことにする。

# In[37]:


a = np.array([[1,2],[3,4]])
np.linalg.eigvals(a)


# ## NumPy使用時によく使う属性とメソッド

# `dir()`を使って`m3`の属性とメソッドを調べてみる。

# In[38]:


dir(m3)


# この中に`transpose()`や`T`があるのが確認できる。この中でよく使うのが`shape`であり，行と列の数を確認する場合に有用なデータ属性である。

# In[39]:


m3.shape


# 2x3の`array`であることが確認できる。
# 
# 次に，抽出した行または列をリストに変換するメソッドについて説明する。

# In[40]:


r0 = mat[0,:]
r0


# これをリストに変換するために`tolist()`というメソッドを使う。

# In[41]:


r0_list = r0.tolist()

r0_list


# In[42]:


type(r0_list)


# ## よく使うNumPy関数

# ### 浮動小数点の比較

# 次のコードを考えよう。

# In[43]:


0.3 == 0.1 + 0.2


# これはバグ（bug）ではない。浮動小数点は近似値として扱われるために発生する（詳細は「[](sec:tip-float)」を参照）。従って，浮動小数点が等しいかを確認するために`==`を使うのは**避けるべきである**。その代わりに`NumPy`の関数`.isclose()`を使うようにしよう。使い方は比べる値を引数に指定するだけで良い。

# In[44]:


np.isclose(0.3, 0.1+0.2)


# ### 様々な`NumPy`関数

# **ルート $\left(\sqrt x\right)$**

# In[45]:


np.sqrt(4)


# **底が$e$の指数関数（$e^x$）**

# In[46]:


np.exp(10)


# **自然対数（$\log_ex$または$\ln x$）**

# In[47]:


np.log(10)


# **`0`が$N$個の`array`を作る。**
# ```
# np.zeros(N)
# ```

# In[48]:


np.zeros(10)


# **`1.0`が$N$個の`array`を作る。**
# ```
# np.ones(N)
# ```

# In[49]:


np.ones(10)


# **$a$から$b$までの区間を等間隔に割った$N$個の数字を返す。**
# ```
# np.linspace(a,b,N)
# ```

# In[50]:


np.linspace(0,1,5)


# **$a$から$b$までの区間で$m$ステップずつ増加し等間隔に割った数字を返す（$b$は含まない）。**
# 
# ```
# np.arange(a,b,m)
# ```
# `m = 1`の場合，組み込み関数の`range(a,b)`と同じ数字を生成するが，返り値が`array`であることが異なる。

# In[51]:


np.arange(5,10,0.5)


# **標本平均**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.mean(x)`$=\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$

# In[52]:


xx = [1,2,3,4,5,6]
np.mean(xx)


# **標本中央値**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.median(x)`

# In[53]:


np.median(xx)


# **標本分散**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.var(x, ddof=0)`$=s_x^2=\dfrac{1}{1-\text{ddof}}\sum_{i=1}^n\left(x_i-\bar{x}\right)^2$（`ddof=0`がデフォルト）
# 
# （注意）計量経済学で習う分散の不偏推定量は`ddof=1`が必要！

# In[54]:


np.var(xx,ddof=1)


# **標本標準偏差**
# 
# `x`が数字の`array`やリストの場合
# 
# `np.std(x, ddof=0)`$=s_x=\sqrt{s_x^2}$  （`ddof=0`がデフォルト）
# 
# （注意）標本標準偏差の場合，必ずしも`ddof=1`により不偏推定量とはならないが，通常`ddof=1`を用いる。

# In[55]:


np.std(xx,ddof=1)


# **標本共分散**
# 
# 2次元以上の`array`やリストの場合
# 
# `np.cov(xy, ddof=0)`$=c_{xy}=\dfrac{1}{1-\text{ddof}}\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})$（`ddof=0`がデフォルト）
# 
# （注意）計量経済学で習う分散の不偏推定量は`ddof=1`が必要！
# 
# 下の計算結果
# 
# * $c_{xy}=-0.6$
# * $s_x^2=3.5$  (\[1,2,3,4,5,6\]の分散）
# * $s_y^2=4.4$  (\[1,6,2,5,3,1\]の分散）

# In[56]:


xy = [[1,2,3,4,5,6],[1,6,2,5,3,1]]
np.cov(xy,ddof=1)


# **標本相関係数**
# 
# 2次元以上の`array`やリストの場合
# 
# `np.corrcoef(xy)`$=r_{xy}=\dfrac{c_{xy}}{s_x\cdot s_y}$
# 
# （注意）`ddof`の影響はない。
# 
# 下の計算結果
# * $r_{xy}=-0.152...$
# * $r_{xx}=r_{yy}=1$

# In[57]:


np.corrcoef(xy)


# ### 効用関数

# 関数に`if`文を組み込む例を考える。相対的リスク回避度一定効用関数は次のように定義される。
# 
# $$
# u(x)=
# \begin{cases}
#     &\dfrac{x^{1-s}-1}{1-s}\quad s\ne 1\\
#     &\log(x)\quad s=1
# \end{cases}
# $$
# 
# `def`を使って表すと次のようになる。

# In[58]:


def utility(x,s):
    
    if s != 1:
        return (x**(1-s)-1) / (1-s)
    
    else:
        return np.log(x)


# In[59]:


utility(10, 1)


# In[60]:


utility(10, 0.2)


# ## `array` vs `list`

# ここでは`list`と`array`の重要な違いについて説明する。
# 次のリストのそれぞれの要素に`10`を足したいとしよう。

# In[61]:


list0 = [1.0, 2.0, 3.0, 4.0, 5.0]


# `for`ループを使うと次のようになる。

# In[62]:


list1 = []

for i in list0:
    list1.append(i + 10)

list1


# 複雑さが残る。また次のコードでは`10`を最後に追加し，リスト同士を結合するだけである。

# In[63]:


list0 + [10]


# より簡単なコードで実行できれば良いが，以下のコードではエラーが発生する。

# In[64]:


list0 + 10


# ---
# これを実現するのが`NumPy`の`array`である。
# 
# まず`array`を作成する。

# In[65]:


arr0 = np.array(list0)
arr0


# In[66]:


arr0 + 10


# この機能はブロードキャスティング（Broadcasting）もしくはベクトル演算（Vectorization）と呼ばれ、ループを使わずに個々の要素に直接働きかけ計算している。この機能により、より高速な計算が可能となるばかりか、より短いコードでそれを実現できる。`+`, `-`, `*`, `**` や他の関数にも同様に使うことができる。以下で例を挙げる。

# In[67]:


arr0 - 5


# In[68]:


arr0 * 10  


# In[69]:


arr0 ** 2


# In[70]:


np.sqrt(arr0)


# In[71]:


np.log(arr0)


# 次の計算も可能である。

# In[72]:


y = arr0 * 2 + np.sqrt(arr0) + 10
y


# この機能は`NumPy`の行列でも有効である。

# In[73]:


mat0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat0


# In[74]:


mat0 * 10


# In[75]:


np.sqrt(mat0)


# In[76]:


np.log(mat0)


# ## マクロ経済学を考える

# ### ケインズの45度線モデル

# * 所得：$Y$
# * 計画支出：$E=C+I+G$
# * 消費関数：$C=d+cY$
#     * 自発的消費：$d=10$
#     * 限界消費性向：$c=0.7$
# * 投資：$I=15$
# * 政府支出：$G=10$
# * 均衡：$E=Y$
# 
# ２つの式で表す。
# 
# $$
# \begin{align*}
#     E-cY &= I+G-d \\
#     E-Y &= 0
# \end{align*}
# $$
# 
# $$\Downarrow$$
# 
# $$
# \begin{bmatrix}
#     1& -c \\
#     1& -1
# \end{bmatrix}
# \begin{bmatrix}
#     E \\
#     Y
# \end{bmatrix}
# =
# \begin{bmatrix}
#     I+G-d \\
#     0
# \end{bmatrix}
# $$

# In[77]:


i = 15   # I
g = 10   # G
d = 10   # d
c = 0.7  # c

a = np.array([[1,-c],[1,-1]])
b = np.array([i+g-d, 0])


# In[78]:


sol = np.linalg.solve(a,b)
print(f'E = {sol[0]:.1f}\nY = {sol[1]:.1f}')


# ### IS曲線の導出：２つの方程式を使う

# #### `for`ループを使う：方法１

# 上の４５度線モデルの投資を次のように変更する。
# * 投資関数：$I=f-hr$
#     * $r$：実質利子率
#     * $f=50$：$r=0$の場合の投資
#     * $h=0.01$：実質利子率が1%上昇した場合，減少する投資量
# * 実質利子率は次の値を取るとする。

# In[79]:


r_list = range(0, 10)
list(r_list)


# それぞれの実質利子率の値での均衡での所得と投資を計算する。まず２つの式で表す。
# 
# $$
# \begin{align*}
#     (1-c)Y-I &= G-d \\
#     I &= f-hr
# \end{align*}
# $$
# 
# $$\Downarrow$$
# 
# $$
# \begin{bmatrix}
#     1-c& -1 \\
#     0& 1
# \end{bmatrix}
# \begin{bmatrix}
#     Y \\
#     I
# \end{bmatrix}
# =
# \begin{bmatrix}
#     G-d \\
#     f-hr
# \end{bmatrix}
# $$

# In[80]:


f = 20.0
h = 1.0


# In[81]:


y_list = []
inv_list = []

for r in r_list:
    
    # 異なる実質利子率の値で解を計算する
    a = np.array([[1-c, -1],[0,1]])
    b = np.array([g-d,f-h*r])
    sol = np.linalg.solve(a,b)
    
    y_list.append(sol[0].round(1))   # round(x)は小数点第x位まで四捨五入するメソッド
    inv_list.append(sol[1])

print('所得：', y_list)
print('投資：', inv_list)


# 実質利子率が上昇すると，所得と投資は減少することがわかる。即ち，IS曲線上では所得と実質利子率は負の関係にあることが確認できる。

# #### `for`ループを使う：方法２

# In[82]:


n = len(r_list)        # r_listの要素数

y_arr = np.zeros(n)    # n個のゼロarray
inv_arr = np.zeros(n)  # n個のゼロarray

for i in range(n):

    a = np.array([[1-c, -1],[0,1]])
    b = np.array([g-d,f-h*r_list[i]])   # i番目のr_listを使う
    sol = np.linalg.solve(a,b)
    
    y_arr[i] = sol[0].round(1)   # i番目のy_arrに割り当てる
    inv_arr[i] = sol[1]          # i番目のinv_arrに割り当てる


print('所得：', y_arr)
print('投資：', inv_arr)


# ### IS曲線の導出：１つの方程式を使う

# 上の２つの式を１つにする。
# 
# $$
# Y=\frac{f-hr+G-d}{1-c}
# $$
# 
# この式を使って`for`ループで計算する。

# In[83]:


y_list = []

for r in r_list:
    
    y = (f-h*r+g-d)/(1-c)
    y = round(y,1)         # round(x)は浮動小数点を四捨五入する関数
    y_list.append(y)

print('所得：', y_list)


# 次の方法でも良い。

# In[84]:


n = len(r_list)        # r_listの要素数

y_arr = np.zeros(n)    # n個のゼロarray

for i in range(n):
    y_arr[i] = (f-h*r_list[i]+g-d)/(1-c)

print('所得：', y_arr.round(1))   # round()は四捨五入するメソッド


# ### IS曲線の導出：ベクトル演算を使う

# `for`ループを使わずに，`array`のベクトル演算を使うともっと簡単なコードで同じ結果を得ることができる。上の１つにまとめた式に基づいて次の関数を定義する。

# In[85]:


def y_equil(r):
    y = (f-h*r+g-d)/(1-c)
    return y.round(1)      # round()は四捨五入のメソッド


# `r_list`を`array`に変換する。

# In[86]:


r_arr = np.array(r_list)
r_arr


# `r_arr`を使って直接評価する。

# In[87]:


print('所得：', y_equil(r_arr))

