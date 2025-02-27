#!/usr/bin/env python
# coding: utf-8

# # Tipsと注意点

# ## 書式について

# コードを書く際に以下を注意すること。

# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Start
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/><input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="translation" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# 1. 分かりやすい変数名を使う。
#     * 具体的な内容を示す変数名は可読性を高める。例えば、インフレ率を`inflation`、インフレ率の変化を`inf_change`。また単位を含めるとより分かりやすくなる。例えば、`kg`や`percent`。`var1`や`var2`と書くと、短くて書きやすいが、他の人や数ヶ月後の自分自身が読み返す時に非常に読み難いコードとなる。
# 1. 変数や関数の命名規則
#     * 名は小文字とアンダースコア`_`を使う（スネーク・スケールと呼ばれる）。
#     * 例えば、`inflation_rate`と書き、`Inflation`や`InflationRate`は避ける。大文字で始まる変数は、慣例としてクラスと呼ばれるオブジェクトに使う。
# 1. エディット・モードのセルでコメントを入れる。
#     * 例えば、`# これはコメントです。`
#     * 目的：可読性を高める。何を書いているかを確認しながらコードを書くことができる。
#     * 行頭にに`#`を挿入することをコメント・アウト（commet out）という。コメント・アウトされたコードは実行されない。
#     * （Tip）行頭に`#`を挿入または削除するトグルのショートカット。
#         * Macの場合、トグルしたい行にカーソルを置き`Command`を押したまま`/`を押下する（`Cmd+/`）。複数行をトグルしたい場合は、それらをハイライトし`Cmd+/`。
#         * Windowsの場合、トグルしたい行にカーソルを置き`Control`を押したまま`/`を押下する（`Ctrl+/`）。複数行をトグルしたい場合は、それらをハイライトし`Ctrl+/`。
# 1. インデントを駆使して可読性を高める。（以下の例で改行は必要ないかもしれないが、１行が長い場合に役立つ）
#     * `(`と`)`の間は改行してもエラーにならない。
#         ```
#         my_func(a = 10,
#                 b = 5,
#                 c = 0)
#         ```
#     * 改行したい箇所に`\`を入れる。（Jupyter Notebookでは`{}`の間に改行を入れてもエラーにならない）
#         ```
#         my_dict = {a:10, \
#                    b:5,  \
#                    c:[1,2]}
#         ```
# 1. スペースや行間を開け読みやすくする。
#     ```
#     # 悪い例
#     def func(x,y):
#         return x*100+y
# 
#     # 良い例
#     def meter_and_centimeter_to_centimer(meter, centimeter):
#         return meter * 100 + centimeter
#     ```

# ## スコープ

# スコープとは、変数が所属し直接アクセスできるコードの中の「領域」を示す。類似する概念に名前空間（Namespace）もあるが、スコープの情報を記す「表」のことであり、スコープ（Scope）と同義と理解すれば良い。
# 
# ここでは基本的に以下のように理解すれば良いであろう。
# 1. Jupyter Notebookを開始した時点から`globalスコープ`が始まる。
# 1. 関数を定義すると、その関数の範囲内で`localスコープ`が生成される。
# 1. 関数の中で入れ子の関数を定義すると、その入れ子関数の範囲内でより狭い`localスコープ`が生成される。
# 1. `globalスコープ`で定義された変数は、`localスコープ`（入れ子関数のより狭い`localスコープ`も含む）からアクセスできるが、`globalスコープ`から`localスコープ`（入れ子関数のより狭い`localスコープ`も含む）の変数にはアクセスできない。
# 1. 関数内の`localスコープ`で定義された変数は、入れ子関数のより狭い`localスコープ`からアクセスできるが、親関数のスコープから入れ子関数の変数にはアクセスできない。
# 
# 次の例を考えよう。

# ### 例１

# In[1]:


s = "Kobe University"  # globalスコープ

def func_1():
    s = "神戸大学"  # localスコープ
    print(s)


# In[2]:


print(s)


# In[3]:


func_1()


# ### 例２

# In[4]:


def func_2():
    a_local = 3
    print(a_local)

func_2()


# `globalスコープ`から`a_local`をアクセスすると次のエラーが発生する。

# In[5]:


a_local


# ### 教訓

# 関数内で使う変数は関数内で定義する方が意図しない結果につながるリスクを軽減できる。この点を説明するために次の例を考えよう。

# In[6]:


a = 10

def func_3(x):
    return a + x

func_3(2)


# **知らずに**以下を設定していたとしよう。

# In[7]:


a = 1000


# In[8]:


func_3(2)


# このような間違いは関数内で変数を定義することで回避できる。

# In[9]:


def func_4(x):
    a = 10
    return a + x

func_4(2)


# ## 浮動小数点型について

# (sec:tip-float)=
# ## 浮動小数点型について

# ### 表記

# `Python`では指数表現がよく使われる。
# 
# `5.123e2`$= 5.123\times 10^{2}$
# 
# `5.123e-2`$= 5.123\times 10^{-2}$
# 
# この例で`5.123`の部分は「仮数」（mantissa もしくは significand）と呼ばれる。

# ## 変数とオブジェクト

# ### 変数とオブジェクトの関係

# `Python`では「全てがオブジェクト」と言われるが、ここでのオブジェクトとは**属性**（**データ**（値や性質など）と**メソッド**（変数特有の関数））から構成される集合体（「塊り」）を指す。例えば、数値`0.1`のオブジェクトを考えよう。`dir()`を使うとどのような属性から構成されているか表示される。

# In[10]:


dir(0.1)


# 例えば、
# * `real`は数値の実数部を示す属性であり、`0.1`の実数数値データである。
# * `as_integer_ratio`は有理数として表すメソッドであり、`（分子、分母）`のタプルとして返す。

# In[11]:


(0.1).real


# In[12]:


(0.1).as_integer_ratio()


# 上の例では、`=`を使い`a`や`x`などの変数に「代入」していないことに注意しよう。これは変数がなくても`0.1`はオブジェクトとして存在していることを示している。では、変数とオブジェクトにはどのような関係があるのだろう。変数`a`を導入するために次のように書いてみよう。

# In[13]:


a = 0.1
a.real, a.as_integer_ratio()


# 以前、次の説明をした。
# 
# > 多くの品物が保管されている大きな倉庫を考えてみよう。管理者はどの品物がどこに保管されているかを記録するための在庫リスト（記録帳やコンピューター・ファイル）を作成し、そこに品物が保管されている棚を示す記号（や番号）を記入しているとしよう。この例では、
# > * オブジェクト　→　倉庫の棚に保管されている品物
# > * 変数　→　在庫リストに記載されている棚の記号
# >
# > となる。即ち、変数は品物の実態とは異なる単なる「参照記号」なのである。
# 
# 
# 上の例の`0.1`がPCのメモリに保存された「品物」であり，`a`は参照記号である。その参照記号を使って，`0.1`の属性`real`にアクセスしたり，メソッド`as_integer_ratio()`を使って有理数として表示している。
# 
# 実は、この考え方（品物と参照記号の関係）は関数の名前とオブジェクトとしての関数の関係にも当てはまる。変数とオブジェクトのこのような関係により、関数がメソッドや関数の引数になることが可能となり、関数の返り値にもなり得るのである。

# ### オブジェクトとメモリー・アドレス

# Pythonのオブジェクトをもう少し考えてみよう。オブジェクトはコンピューター内のメモリに保存され、直ぐに計算などに使えるように準備されている。例えば、`0.1`というオブジェクトを生成してみる。

# In[14]:


a = 0.1


# コンピューター・メモリーには住所のようにロケーションを示すメモリー・アドレス（以下では「アドレス」と呼ぶ）があり、`id()`関数を使うとそれを表示することができる。

# In[15]:


id(a)


# ２つのオブジェクトが同一のものかどうかを確認するには、このアドレスを比べれば良い。例えば、`a`と同じオブジェクトを示す別の参照記号`b`を生成しよう。

# In[16]:


b = a


# In[17]:


id(b)


# アドレスが同じなので同じオブジェクトであることが確認できる。また、アドレスが等しいかどうかは`is`を使って確認することもできる。

# In[18]:


a is b


# `==`ではないことに注意しよう。`==`は`10`という値が同じかどうかを確認するだけで、アドレスとは無関係である。

# In[19]:


c = 0.1
id(c)


# In[20]:


c is a, c == a


# 整数では$[-5,256]$以外この結果が成り立つ。$[-5,256]$は処理速度を最適化するために、Pythonのセッションが始まると同時に自動でメモリーにキャッシュ（保存）されるためアドレスは同じになる。例えば、次の`d`と`e`は値もアドレスも同じである。

# In[21]:


d = 1
e = 1
d is e, d == e


# 次に関数を考えてみよう。

# In[22]:


def func(x):
    return x**2

func(2)


# この関数のアドレスも`id()`を使い確認できる。

# In[23]:


id(func)


# ＜注意＞
# 
# * `id(func())`とするとエラーが発生する。`()`を付けると「関数を評価する」ためである。
# * `id(func(2))`とするとエラーは発生しないが、`func(2)`を評価した結果（即ち、`4`）のアドレスを表示することになる。
# * `func`は関数の「参照記号」であり、それを引数とすることにより関数のアドレスが表示される。

# ### 「浅いコピー」と「深いコピー」

# オブジェクトと変数の関係は、倉庫に保管されている商品と参照番号の関係と同じだと説明した。このような関係により、次のような問題が発生する。

# In[24]:


f = [1,2,3]
f


# リスト`f`のコピーである`g`を作成する。

# In[25]:


g = f


# `g`と`f`は同じオブジェクトであり、`is`で確認できる。

# In[26]:


g is f, id(g), id(f)


# 即ち、`g`と`f`は別の参照記号ではあるが同じ品物を指している。ここで、`f`にメソッド`append()`を使って`100`を追加しよう。

# In[27]:


f.append(100)
f


# `g`はどうなっているかというと

# In[28]:


g


# `f`と`g`は同じ品物を指している参照番号なので、このような結果となる。
# 
# `100`が追加された後のアドレスを表示してみよう。

# In[29]:


f is g, id(f), id(g)


# `100`が追加される前のアドレスと同じである。即ち、`append()`は元のオブジェクトを変化させている。このようなことが発生することを念頭に置いて`f=g`のようなコードを書くべきであり、このことを忘れると意図しない結果につながる。このようなリスクを回避するためには、同じ数値のコピーを異なるオブジェクトとして生成する必要がある。そのためにはメソッド`.copy()`を使う。

# In[30]:


f_copy = f.copy()
f_copy


# In[31]:


f_copy is f


# `.copy()`で生成したコピーは
# **「浅いコピー」**
# （shallow copy）と呼ばれる。しかし、浅いコピーの場合でも、リストが二重配列（入れ子）になっている場合は上で説明した同じ問題が発生する。その場合には、標準ライブラリ`copy`の`deepcopy`関数を使い独立したコピーを作ることが可能となる。これを
# **「深いコピー」**
# （deep copy）呼ぶ。

# In[32]:


from copy import deepcopy
f_deep = deepcopy(f)
f_deep


# **＜以下の場合にリストの浅いコピーが生成される＞**
# 1. メソッド`.copy()`によるコピー
# 1. `list()`関数によるコピー
# 1. リストのインデクシング（indexing）およびスライシング（slicing）によるコピー

# In[33]:


# list()による浅いコピー
ff1 = list(f)
ff1, ff1 is f


# In[34]:


# インデクシング
ff2 = f[1]
ff2, ff2 is f


# In[35]:


# スライシング
ff3 = f[:]
ff3, ff3 is f


# ## NumPy：ビューとコピー

# リストの「浅いコピー」と「深いコピー」の問題は`NumPy`にも存在する。しかし、これも`np.copy()`関数や`array`型のメソッド`.copy()`で回避することができる。また類似する問題としてコピー（copy）とビュー（view）の違いがある。以下ではこの問題を説明する。

# In[36]:


import numpy as np


# In[37]:


arr = np.array([1,2,3,4,5])
arr


# これをスライスして異なる変数を参照記号として使う。

# In[38]:


arr_slice = arr[1:3]
arr_slice


# `arr_slice`の`2`を`200`に入れ替える。

# In[39]:


arr_slice[0] = 200
arr_slice


# `arr`を表示しよう。

# In[40]:


arr


# `arr_slice`を変更したにも関わらず、`arr`も影響を受けている。これは`arr_slice`と`arr`が参照している元のデータが同じであるために発生する。即ち、`arr`は元のデータ全てを表示し、`arr_slice`は同じデータの一部を表示しているのである。`arr_slice`を`arr`のビュー（view）と呼ぶ。
# 
# ```{warning}
# `arr[0] is arr_slice[1]`としても`False`となる。リストと異なり、`np.array`ではそれぞれの要素がメモリーに配置されていないため、`indexing`でアクセスする度に結果をメモリーに配置することになる。したがって`arr[0]`でアクセスするとその結果があるアドレスに配置され、続く`arr_slice[1]`は別のアドレスに保存されることになり`False`が返される。
# ```

# ---
# ではどのような場合に`views`になるのか。残念ながら、複雑な場合分けが必要になり、それを覚え使いこなすにはある程度の慣れが必要だる。従って、`view`をどうしても使わなくてはならない状況を除いては、以下のようにメソッド`.copy()`を使い、コピーを生成して作業することを強く推奨する。`.copy()`は「深いコピー」を生成する。

# In[41]:


arr_copy = arr[1:3].copy()
arr_copy


# `arr_copy`の`3`を`300`に入れ替える。

# In[42]:


arr_copy[1] = 300
arr_copy


# In[43]:


arr


# `arr`は影響を受けていない。
# 
# ＜コメント＞
# 
# `view`の役目はなんなのか、という疑問が生じる。`.copy()`は新たにオブジェクトを生成するが、`view`であれば新たなオブジェクトを生成する必要がない。その分、処理速度が早くなるのである。しかし、実証分析で行う「通常」のデータ処理であれば`.copy()`を使って問題ないだろう。

# ## Pandas：ビューとコピー

# `NumPy`と同じように`Pandas`もビュー（view）とコピー（copy）の問題が存在する。確認するために、次のコードを考えよう。

# In[44]:


import pandas as pd
df = pd.DataFrame({'a':np.arange(4), 'b':np.arange(4)})
df


# In[45]:


df_slice = df.iloc[1:3,:]
df_slice


# `.iloc[]`により`view`が生成されている。
# 
# それを確認するために元の`DataFrame`である`df`の要素を変更する。

# In[46]:


df.iloc[1,1] = 100
df


# In[47]:


df_slice


# ここではスライシングで生成した場合を考えたが、他の場合でも`view`になったり`copy`になったりする。実は、`NumPy`と同様に場合わけが複雑だが、`NumPy`の場合よりも`view`なのか`copy`なのかの判別が非常に難しい。しかし、`Pandas`は`view`**かもしれない**`DataFrame`や`Series`に変更を加えると警告を出す仕組みになっている。`df_slice`を使って説明する。
# 
# ```
# df_slice.iloc[1,0] = 200
# ```
# とすると次のような警告が出る。
# ```
# /Users/my_name/anaconda3/envs/py4etrics/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame
# 
# See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   """Entry point for launching an IPython kernel.
# ```

# この警告が出る場合は、`view`の疑いが高い（確定ではない）ので、`df`のメソッド`.copy()`を使って「深いコピー」を生成することを薦める。以下の例を考えよう。

# In[48]:


df_copy = df.copy().iloc[1:3,:]
df_copy


# In[49]:


df.iloc[2,1] = 2000
df


# In[50]:


df_copy


# In[51]:


df_slice


# `df_copy`は影響を受けていないが、`df_slice`の値は元のデータの変化を反映している。
