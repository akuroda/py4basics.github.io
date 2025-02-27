#!/usr/bin/env python
# coding: utf-8

# (chap:pandas_plot)=
# # `Pandas`：図示

# ## 説明

# In[1]:


import pandas as pd
import numpy as np
import japanize_matplotlib


# ```{margin}
# <div name="html-admonition">
# Do you want to read in a differnt language? Start
# <input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="Google" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/><input type="button" onclick="location.href='https://translate.google.com/translate?hl=&sl=ja&tl=en&u='+window.location;" value="translation" style="color:#ffffff;background-color:#008080;" onmouseover="this.style.background='#99ccff'" onmouseout="this.style.background='#008080'"/>
# in English or the language of your choice.
# </div>
# ```

# プロット用のパッケージ`Matplotlib`を紹介したが，実は`Pandas`の`DataFrame`と`Series`にはメソッド`plot()`が備えられており，それを使えば基本的なプロットをより簡単んコードで実現できる。裏で動いているのは`Matplotlib`であり，より複雑な図を作成する場合は、`Matplotlib`のコードを直接書くことが必要になるだろうが，手っ取り早くプロットしたい場合には重宝する手法である。詳細は[参考サイト（英語）](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)を参考にして欲しいが，ここでは基本的な使い方を紹介する。

# 次の`df0`を使って説明する。

# In[2]:


dic = {'X':[10, 20, 30],
       'Y':[5.0, 30.0, 15.0],
       'Z':[3.0, 2.0, 5.0]}
df0 = pd.DataFrame(dic)
df0


# ## プロット方法

# プロット方法は簡単で，メソッド`.plot()`を使うと全ての列がプロットされる。

# In[3]:


df0.plot()


# * デフォルトでは横軸に行インデックスが使われ、`float`として扱われて表示されている。
# * 凡例は自動的に表示され、列ラベルが使われる。
# * 図の上に文字が表示されるが，表示したくない場合は最後に`;`を加えるか次の行に`pass`と書くと良いだろう。
# 
# 次にある列だけをプロットしたい場合を考えよう。その場合は，プロットしたい列を抽出しメソッド`plot()`を使う。選択には`[]`を使い，その中に列ラベルをリストとして指定する。まず１つの列を選択する場合を考えよう。例えば，`X`を選択するとしよう。この場合、２つの方法がある。
# 
# * `X`を`Series`として抽出する場合
#     ```
#     df0['X']
#     ```
# * `X`を`DataFrame`として抽出する場合
#     ```
#     df0[['X']]
#     ```
#     ここでは`X`をリスト`['X']`として使っている。
#     
# 列ラベルは文字列`X`で指定していることに留意しよう。
# 
# まず`X`の`Series`として抽出しよう。

# In[4]:


df0['X']


# 次に`X`を`DataFrame`として抽出する。

# In[5]:


df0[['X']]


# 表示が少し異なることが確認できるが，メソッド`plot()`でも少しだけ違いがある。まず`X`を`Series`としてプロットしてみる。

# In[6]:


df0['X'].plot()
pass


# `X`を`DataFrame`としてプロットすると凡例も表示される。

# In[7]:


df0[['X']].plot()
pass


# この場合の凡例は列ラベルがそのまま使われている。
# 
# 次に`X`と`Z`をプロットしたいとしよう。２つの列を抽出するためには，以下のように列ラベルをリストとして書く。

# In[8]:


df0[['X','Z']]


# メソッド`plot()`を使いプロットする。

# In[9]:


df0[['X','Z']].plot()
pass


# もしくは`Series`を2行に分けても同じ図となるが，凡例は表示されない。

# In[10]:


df0['X'].plot()
df0['Z'].plot()
pass


# デフォルトでは横軸に行インデックが使われるが，横軸を指定したい場合は，次の引数を使う。
# * `x`：横軸に使う列ラベル
# * `y`：縦軸に使う列ラベル（複数の場合はリスト）

# In[11]:


df0.plot(x='X',y=['Y','Z'])
pass


# ## 引数とメソッド

# (sec:5-options)=
# ## 引数とメソッド

# ### 基本的な引数

# `plot()`には様々な引数があり図に「飾り付け」をすることができる。詳しくは[このリンク](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html)を参照することにして，ここでは基本的な引数だけを紹介する。
# <!-- * `title`：図のタイトル（文字列型で指定） -->
# * `style`：線のスタイル（複数ある場合はリストにして列の順番で指定する;`-``--``-.``:`）
# * `linewidth` or `lw`：線の幅
# * `color`：色（リストにして列の順番で指定する; [参照サイト](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)）
#     * `r`は赤
#     * `k`は黒
#     * `g`はグリーン
# * `marker`：観測値のマーカー（`o`，`.`，`>`，`^`などがある; [参照サイト](https://matplotlib.org/3.2.2/api/markers_api.html)）
# * `markersize`：マーカーの大きさ
# * `fontsize`：横軸・縦軸の数字のフォントサイズの設定
# * `figsize`：図の大きさ
#     * `figsize=(キャンバスの横幅、キャンバスの縦の長さ)`
# * `legend`：凡例の表示を指定
#     * `DataFrame`の場合はデフォルトは`True`
#     * `Series`の場合はデフォルトは`False`
#     * 複数の図を表示する際は下で説明する「軸」のメソッドとして指定することもできる。
# * `label`：凡例の表現を指定（`Series`のみ有効）
# * `grid`：グリッド表示（ブール型;デフォルトは`False`)
#     * 複数の図を表示する際は，この引数は使わずに下で説明する「軸」のメソッドとして指定する。
# * `ax`：プロットする「軸」を指定する。
#     * １つの「軸」に複数の図を表示する際に使う（後で使い方を説明する）。

# In[12]:


# df0はDataFrame

df0.plot(style=[':','--','-'],
         linewidth=2,
         color=['r','k','g'],
         marker='o',
         markersize=10,
         fontsize=15,
         figsize=(8, 4),   # 8は横軸、4は縦軸のサイズ
         legend=False,
         grid=True,
        )
pass


# ### タイトルとラベルのサイズの調整

# (sec:5-titlelabels)=
# ### タイトルとラベルのサイズの調整

# タイトルのフォント・サイズの指定，横軸と縦軸のラベルとフォント・サイズの指定をおこなう場合は、`plot()`の引数ではなく下で説明する方法でおこなう。この方法を理解するために、`Pandas`（実は`Matplotlib`）が表示する図は{numref}`fig:5-figure_axes`で示している階層的な構造となることをイメージして欲しい。ここで重要なのは「キャンバス」と「軸」の違いである。
# 
# ```{figure} /images/figure_axes_pandas.png
# ---
# scale: 40%
# name: fig:5-figure_axes
# ---
# 「キャンバス」と「軸」の関係
# ```
# 
# 1. 「キャンバス」とは実際に表示される**領域**であり，実際には表示されない「透明のキャンバス」である。
#     * `figure`や`fig`などの変数名や引数名があれば、「キャンバス」を指していると理解すれば良いだろう。
# 1. 「軸」とは１つの図を表示する「キャンバス」上の**区域**である。
#     * `ax`や`axes`などの変数名があれば、「軸」を表していると理解すれば良いだろう。
#     * 「キャンバス」上に複数の図を表示する場合は複数の「軸」が必要となる。
#     * 「軸」に図のタイトルや縦軸・横軸のラベルなどを追加することになる。
#     
# 「軸」の中にメソッド`.plot()`を使いグラフを表示することになる。

# 従って，概ね次のように理解して良いだろう。
# * 上で説明した「基本的な引数」は上の図のピンクのエリア内での変更となる。
#     * `figsize`は「キャンバス」の大きさを指定する引数だが，メソッド`plot()`は自動で「キャンバス」を作成するため`plot()`内で変更できるようになっている。
# * タイトルや縦・横軸ラベルは「軸」のメソッドを使い変更する。
# 
# では実際に手順を説明する。
# * `df0.plot()`は自動で「キャンバス」と「軸」を作成すると同時に「軸」を返す。それを変数（例えば，`ax`）に割り当てる。
# * `ax`のメソッドを使って以下を設定する。
#     * タイトル：`.set_title()`
#     * 横軸ラベル：`.set_xlabel()`    
#     * 縦軸ラベル：`.set_ylabel()`
# 
# 実際にそれらの引数を使ってプロットしてみよう。

# In[13]:


ax = df0.plot(
              grid=True,
              style=[':','--','-'],
              marker='o',
              fontsize=15,
             )
ax.set_title('A Large Title', size= 30)     # タイトルの設定
ax.set_xlabel('Horizontal Axis', size=20)   # 横軸ラベルの設定
ax.set_ylabel('Vertical Axis', size=20)     # 縦軸ラベルの設定
pass


# ### 「軸」を指定してプロットする場合

# 上で「軸」のメソッドとしてタイトルなどを追加できることを説明したが，`plot()`の引数として「軸」を指定して図を追加することができる。次のコードを考えてみよう。

# In[14]:


ax_ = df0[['X','Y']].plot()  # 1行目
df0[['Z']].plot(ax=ax_)      # 2行目
pass


# １行目の右辺では「キャンバス」と「軸」が自動生成され，その内「軸」のみが返され変数`ax_`に割り当てられている。２行目の`plot()`の引数`ax`は「軸」を指定する引数であり，それに`ax_`を設定している。即ち，`Z`を「軸」`ax_`にプロットすることを指定している。このコードには２つの利点がある。
# 1. `X`と`Y`と異なる「飾り付け」を`Z`に簡単に施すことができる。
# 1. ２行目に`df0`ではなく別の`DataFrame`を使うことも可能となる。
# 
# もちろん，タイトルや軸ラベルのメソッドをつか加えることも可能である。

# In[15]:


ax_ = df0[['X','Y']].plot(marker='o',markersize=10)
df0[['Z']].plot(ax=ax_, marker='^',markersize=15)
ax_.set_title('This is a title', size=20)
ax_.set_xlabel('Horizontal axis', size=15)
ax_.set_ylabel('Vertical axis', size=15)
ax_.grid()
ax_.legend(['Xの凡例','Yの凡例','Zの凡例'])
pass


# また上のコードの最後に２行を付け加えているので便利なので参考にして欲しい。
# * `ax_.grid()`：グリッド線を表示するメソッド。
#     * １つの「軸」に`plot`を複数回適用する場合，個々の`plot`の引数`grid=True`を使わず`ax_.grid()`を指定する。
# * `ax_.legend(['Xの凡例','Yの凡例','Zの凡例'])`
#     * 凡例に列ラベルではなく他の表現を指定いたい場合に使う。

# ### 図を並べる

# 図を縦に並べるには`subplots=True`を指定する。

# In[16]:


df0.plot(subplots=True)
pass


# 図を横に並べるには`layout=(1,3)`を付け加える。`layout`は図の配置を行列のように考えて指定し、`1`は行の数であり、`3`は列の数。
# ```
# layout(行の数、列の数)
# ```

# In[17]:


df0.plot(subplots=True, layout=(1,3), figsize=(8,3))
pass


# ### ２軸グラフ

# 左軸を`X`と`Y`に，右軸を`Z`に使うとしよう。その場合，引数`secondary_y`に`Z`を設定する。

# In[18]:


df0.plot(secondary_y='Z')
pass


# 別々の飾り付けをする場合は次のようにすると良いだろう。

# In[19]:


ax_ = df0[['X','Y']].plot()
df0[['Z']].plot(marker='x', markersize=10, linestyle=':',
                secondary_y=True, ax=ax_)
pass


# 上の図との主な違いが３行目にある
# * `secondary_y=True`：`Z`を右軸に使うことを指定する。
# * `ax=ax_`：「軸」`ax_`に`Z`をプロットする。

# ## 日本語

# ２つ方法を紹介するが、`japanize_matplotlib`を使う方法がより簡単であろう。

# ### `japanize_matplotlib`

# 使い方は到って簡単で、`Pandas`と同様にインポートするだけである。

# In[20]:


import japanize_matplotlib


# In[21]:


ax = df0.plot(grid=True
             ,style=[':','--','-']
             ,marker='o'
             ,fontsize=15
             )
ax.set_title('縦横タイトル', size= 30)
ax.set_xlabel('横軸', size=20)
ax.set_ylabel('縦軸', size=20)
pass


# ### フォントを指定する

# 2つの方法：
# 1. フォントはインストールせず、PC内にあるフォントを指定する。
# 1. フォントをインストールする方法

# 方法１の場合、以下で説明に使う変数`jfont`にフォントを指定する。
#     * Macの場合、例えば`AppleGothic`
#     * Windowsの場合、例えば`Yu Gothic`
#     * この方法では一部の日本語が文字化けする場合がある。
# 
# 方法２の場合：
# * [このサイト](https://ipafont.ipa.go.jp/node193#jp)から次の内の１つをダウンロードする。
#     * 2書体パック(IPAex明朝(Ver.xxx)、IPAexゴシック(Ver.xxx))
#     * IPAex明朝 (Ver.xxx)
#     * IPAexゴシック(Ver.xxx)
# * [このサイト](https://ipafont.ipa.go.jp/node72#jp)に従ってインストールする。
# * 次の両方もしくは１つがPCにインストールされる
#     * IPAexMincho（IPAex明朝）
#     * IPAexGothic（IPAexゴシック）
# 
# 上の例を使い、設定方法の例を示す。

# In[22]:


jfont = 'IPAexGothic'    # (1)

ax = df0.plot(grid=True
             ,style=[':','--','-']
             ,marker='o'
             ,fontsize=15
             )
ax.set_title('縦横タイトル', size= 30, fontname=jfont)   # (2)
ax.set_xlabel('横軸', size=20, fontname=jfont)          # (3)
ax.set_ylabel('縦軸', size=20, fontname=jfont)          # (4)
ax.legend(prop={'family':jfont, 'size':17})            # (5)
pass


# >* (1) 使用するフォントを`jfont`に割り当てる。
# >* (2) 引数`fontname`で`jfont`を指定する。タイトルのフォントが変更される。
# >* (3) 引数`fontname`で`jfont`を指定する。横軸名のフォントが変更される。
# >* (4) 引数`fontname`で`jfont`を指定する。縦軸名のフォントが変更される。
# >* (5) `legend`は他と設定方法が異なる。
#     * `prop`はフォントのプロパティを設定する引数であり、辞書で指定する。
#     * キー`family`に値`jfont`を指定する。凡例のフォントが変更される。
#     * キー`size`に数値を設定してフォントの大きさが変更される。

# この例では個別にフォントを設定したが、一括で全てのフォントを変更する方法もあるが説明は割愛する。

# ## マクロ経済学の例

# ### 投資関数

# 実質利子率`r`によって投資がどのように変化するかを考えてみよう。まず投資関数を次のように仮定する。

# In[23]:


def investment(r):
    return 100/(1+r)**50


# * `100`：実質利子率が`0`の場合の投資
# 
# 実質利子率は次の`array`で与えられるとする。

# In[24]:


r_arr = np.arange(0.01,0.11,0.01)
r_arr


# 次に関数`investment`と`r_arr`を使い投資の`array`を作成しよう。

# In[25]:


inv_arr = investment(r_arr)
inv_arr


# これらのデータを使い`DataFrame`を作成する。

# In[26]:


df_inv = pd.DataFrame({'investment':inv_arr,
                       'interest_rate':r_arr})


# 最初の5行を表示する。

# In[27]:


df_inv.head()


# ではプロットしてみよう。

# In[28]:


df_inv.plot('interest_rate','investment')
pass


# ### 将来価値

# `x`万円を実質年率`r`%の利息を得る金融商品に投資し，`t`年間の将来価値（期首の値）をリストで示す関数は以下で与えられた。

# In[29]:


def calculate_futre_value(x, r, t):
    
    value_list = [x]           # 初期値が入ったリスト
    
    for year in range(1,t+1):  # 1からtまでの期間
        x = x*(1+r)            # 来期のxの値の計算
        value_list.append(x)   # リストに追加
    
    return value_list          # リストを返す


# これを使い，
# * `x`=`100`
# * `t`=`30`
# 
# の下で実質利子率が次のリストで与えられる値を取る場合の将来価値を図示する。

# In[30]:


r_list = [0.01, 0.03, 0.06]   # 実質利子率のリスト
dic = {}                      # 空の辞書

for r in r_list:
    dic['r='+str(r)] = calculate_futre_value(100, r, 30)  # 辞書に追加

df_future = pd.DataFrame(dic) # DataFrameの作成


# `dic['r='+str(r)]`の説明：
# * `str(r)`：`r_list`の要素のダミーである`r`は浮動小数点型なので関数`str()`を使って文字列型に変換する。
# * `'r='+str(r)`：文字列型の`r=`と文字列型の`str(r)`を`+`で結合する。
# * `dic['r='+str(r)]`：辞書`dic`にキー・値のペアを作成する。
#     * キー：`'r='+str(r)`
#     * 値：`calculate_futre_value(100, r, 30)`の返り値

# 最初の5行を表示する。

# In[31]:


df_future.head()


# 最後の5行を表示する。

# In[32]:


df_future.tail()


# In[33]:


df_future.plot()
pass


# ## その他のプロット

# ### 種類

# メソッド`.plot()`には様々な引数が用意されているが，その中に`kind`がある。次を文字列として指定すると様々な種類のプロットが可能となる。
# * `line`：ライン・プロット
#     * デフォルトの値であり，上で説明した直線・曲線のプロットとなる。
#     * `.plot()`は`.plot.line()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html)
# * `bar`：縦向きの棒グラフ（カテゴリーなどの離散変数に使う）
#     * `.plot(kind='bar')`は`.plot.bar()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)
# * `barh`：横向き棒グラフ（カテゴリーなどの離散変数に使う）
#     * `barh`の`h`はHorizontalのH
#     * `.plot(kind='hbar')`は`.plot.hbar()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html)
# * `hist`：ヒストグラム（連続変数に使う）
#     * `hist`はHISTogramのHIST
#     * `.plot(kind='hist')`は`.plot.hist()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html)
# * `box`：ボックスプロット
#     * `.plot(kind='box')`は`.plot.box()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html)
# * `kde`：カーネル密度推定プロット
#     * `kde`はKernel Density EstimateのKDE
#     * `.plot(kind='kde')`は`.plot.kde()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.kde.html)
# * `density`：`kde`と同じ
# * `area`：エリア・プロット
#     * `.plot(kind='area')`は`.plot.area()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.area.html)
# * `pie`：パイチャート
#     * `.plot(kind='pie')`は`.plot.pie()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html)
# * `scatter`：散布図（`DataFrame`のみ）
#     * `.plot(kind='scatter')`は`.plot.scatter()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html)
# * `hexbin`： : 六角形プロット（`DataFrame`のみ）
#     * `.plot(kind='hexbin')`は`.plot.hexbin()`と同じでもある。
#     * [プロットの例](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html)

# 上で説明した[ライン・プロットの引数](sec:5-options)は他のプロットと共通のものが多いが，それぞれ独自の引数もある。
# 
# 以下では散布図，ヒストグラム，カーネル密度推定プロット，棒グラフについて説明する。
# 
# 説明には次のコードで生成する`DataFrame`を使う。列`X`と`Y`には標準正規分布（平均`0`，標準偏差`1`）から生成した100個のランダム変数が含まれている。`Z`には正規分布（平均`2`，標準偏差`1`）から抽出した100個のランダム変数が格納されている。

# In[34]:


df1 = pd.DataFrame({'X':np.random.normal(size=100),
                    'Y':np.random.normal(size=100),
                    'Z':np.random.normal(loc=2, size=100)})


# `X`，`Y`は同じ標準正規分布から生成されているが，異なる値から構成されている。

# ### 散布図

# 散布図をプロットする場合は次の構文となる。
# ```
# df1.plot(＜横軸の列ラベル＞, ＜縦軸の列ラベル＞, kind='scatter')
# ```
# 列`X`と`Y`を使ってプロットしてみよう。

# In[35]:


df1.plot('X', 'Y', kind='scatter')
pass


# **＜基本的な引数＞**
# 
# 様々な引数があり図に「飾り付け」をすることができる。詳しくは[このリンク](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html)を参照することにして，ここでは基本的な引数だけを紹介する。
# * `title`：図のタイトル（文字列型で指定）
# * `color`：色（リストにして列の順番で指定する; [参照サイト](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)）
#     * `r`は赤
#     * `k`は黒
#     * `g`はグリーン
# * `marker`：観測値のマーカー（`o`，`.`，`>`，`^`などがある; [参照サイト](https://matplotlib.org/3.2.2/api/markers_api.html)）
# * `s`：マーカーの大きさ（`markersize`ではない！）
# * `fontsize`：横軸・縦軸の数字のフォントサイズの設定
# * `figsize`：図の大きさ
#     * `figsize=(キャンバスの横幅、キャンバスの縦の長さ)`
# * `legend`：凡例の表示を指定
#     * `DataFrame`の場合はデフォルトは`True`
#     * `Series`の場合はデフォルトは`False`
# * `label`：凡例の表現を指定（`Series`のみ有効）
# * `grid`：グリッド表示（ブール型;デフォルトは`False`)
# * `ax`：プロットする「軸」を指定する。

# In[36]:


# df1はDataFrame

df1.plot('X', 'Y', kind='scatter',
         title='タイトルです',
         color='red',
         marker='^',
         s=100,
         fontsize=20,
         figsize=(8,4),
#          legend=True,
         label='Y',
         grid=True
        )
pass


# この図ではタイトルと横軸・縦軸ラベルの大きさが調整できていないが，上で説明した[タイトルとラベルのサイズの調整](sec:5-titlelabels)のコードと共通なので，そちらを参照しよう。

# またライン・プロットと同じように引数`ax`を使うことにより，複数の散布図を重ねてプロットできる。次のコードは`X`と`Y`，そして`X`と`Z`の散布図を同じ「軸」に表示している。

# In[37]:


# df1はDataFrame

ax_ = df1.plot('X', 'Y', kind='scatter',label='Yのデータ')
df1.plot('X', 'Z', kind='scatter',
         color='red', marker='^', label='Zのデータ', ax=ax_)
pass


# ### ヒストグラム

# ヒストグラムは次の構文となる。
# ```
# df1.plot(kind='hist')
# ```
# この場合，`df1`にある全ての列（整数型もしくは浮動小数点型）がヒストグラムとして重ねて表示される。特定の列だけを使う場合は次のように列を選択して`plot()`を使おう。

# In[38]:


# df1['Y']はSeries

df1['Y'].plot(kind='hist')
pass


# **＜基本的な引数＞**
# 
# 様々な引数があり図に「飾り付け」をすることができる。詳しくは[このリンク](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html)を参照することにして，ここでは基本的な引数だけを紹介する。
# * `title`：図のタイトル（文字列型で指定）
# * `bins`：柱の数
# * `color`：色（リストにして列の順番で指定する; [参照サイト](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)）
#     * `r`は赤
#     * `k`は黒
#     * `g`はグリーン
# * `edgecolor`又は`ec`：柱の境界線の色
# * `alpha`：透明度（`0`から`1.0`; デフォルトは`1`）
# * `density`：縦軸を相対度数にする（デフォルトは`False`）
#     * 全ての柱の**面積**の合計が`1`になるように縦軸が調整される。１つの柱の高さが`1`よりも大きくなる場合もある。
# * `fontsize`：横軸・縦軸の数字のフォントサイズの設定
# * `figsize`：図の大きさ
#     * `figsize=(キャンバスの横幅、キャンバスの縦の長さ)`
# * `legend`：凡例の表示を指定
#     * `DataFrame`の場合はデフォルトは`True`
#     * `Series`の場合はデフォルトは`False`
# * `label`：凡例の表現を指定（`Series`のみ有効）
# * `grid`：グリッド表示（ブール型;デフォルトは`False`)
# * `subplots`：複数の図をプロットする（詳細はライン・プロットを参照）
# * `ax`：プロットする「軸」を指定する。

# 引数を指定して`X`のヒストグラムをプロットしてみよう。

# In[39]:


# XはSeriesとして抽出されている

df1['X'].plot(kind='hist',
         bins=20,
         title='タイトルです',
         color='red',
         ec='white',
         alpha=0.5,
         density=True,
         fontsize=20,
         figsize=(8,4),
         legend=True,
         label='Xの凡例',
         grid=True
        )
pass


# この図ではタイトルと横軸・縦軸ラベルの大きさが調整できていないが，上で説明した[タイトルとラベルのサイズの調整](sec:5-titlelabels)のコードと共通なのでそちらを参照しよう。

# 次に複数のデータを重ねてプロットする場合を考えよう。ここで役に立つ引数が`alpha`である。

# In[40]:


df1[['Y','Z']].plot(kind='hist',
                    bins=30,
                    color=['r','k'],
                    edgecolor='k',
                    alpha=0.4)
pass


# 濃い部分が重なっている部分となる。また柱を積み上げて表示するには`stacked=True`（デフォルトは`False`）を使う。

# In[41]:


df1[['Y','Z']].plot(kind='hist', 
                    bins=30,
                    color=['r','k'],
                    edgecolor='white',
                    stacked=True)
pass


# 赤の上に黒が積み上げられている。

# ### カーネル密度推定プロット

# (sec:5-kernel)=
# ### カーネル密度推定プロット

# ヒストグラムは縦軸に度数，横軸に階級を取ったグラフだが，関連する手法にカーネル密度推定と呼ばれるものがある。考え方は簡単で，上のようなヒストグラムのデータに基づき面積が１になるようにスムーズな分布を推定する手法である。ヒストグラムとカーネル密度関数を重ねてプロットすることもできる。
# 
# 次の構文となる。
# ```
# df1.plot(kind='kde')
# ```
# この場合，`df1`にある全ての列がヒストグラムとして重ねて表示される。特定の列だけを使う場合は列を選択して`plot()`を使う。

# In[42]:


df1.plot(kind='kde')
pass


# **＜基本的な引数＞**
# 
# 様々な引数があり図に「飾り付け」をすることができる。詳しくは[このリンク](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.kde.html)を参照することにして，ここでは基本的な引数だけを紹介する。
# * `title`：図のタイトル（文字列型で指定）
# * `linestyle`又は`style`：線のスタイル（リストにして列の順番で指定する;`-``--``-.``:`）
# * `linewidth` or `lw`：線の幅
# * `color`：色（リストにして列の順番で指定する; [参照サイト](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)）
#     * `r`は赤
#     * `k`は黒
#     * `g`はグリーン
# * `alpha`：透明度（`0`から`1.0`; デフォルトは`1`）
# * `fontsize`：横軸・縦軸の数字のフォントサイズの設定
# * `figsize`：図の大きさ
#     * `figsize=(キャンバスの横幅、キャンバスの縦の長さ)`
# * `legend`：凡例の表示を指定
#     * `DataFrame`の場合はデフォルトは`True`
#     * `Series`の場合はデフォルトは`False`
# * `label`：凡例の表現を指定（`Series`のみ有効）
# * `grid`：グリッド表示（ブール型;デフォルトは`False`)
# * `ax`：プロットする「軸」を指定する。

# 引数を指定して`X`をプロットしてみる。

# In[43]:


# XはSeriesとして抽出されている

df1['X'].plot(kind='kde',
         title='タイトルです',
         linewidth=5,
         linestyle='-.',
         color='red',
         alpha=0.5,
         fontsize=20,
         figsize=(8,4),
         legend=True,
         label='Xの凡例',
         grid=True
        )
pass


# この図ではタイトルと横軸・縦軸ラベルの大きさが調整できていないが，上で説明した[タイトルとラベルのサイズの調整](sec:5-titlelabels)のコードと共通なのでそちらを参照しよう。

# 次にヒストグラムとカーネル密度推定プロットを重ねて図示してみる。ここで重要な点がヒストグラムに引数`density=True`を設定することである。これがないと縦軸の単位が異なり上手く表示できない。

# In[44]:


ax_ = df1['X'].plot(kind='hist',
                    density=True,
                    label='Xのヒストグラム',
                    legend=True)
df1['X'].plot(kind='kde',
              ax=ax_,
              label='XのKDE',
              legend=True)
pass


# ### 縦線・横線

# 図に縦線や横線を追加したい場合がある。その場合は，[タイトルとラベルのサイズの調整](sec:5-titlelabels)にあるように「軸」に追加していく事になる。次のような書き方となる。
# 
# * 縦線の場合
#     ```
#     ax_.axvline(＜横軸の値＞)
#     ```
#     ここで`axvline`の`ax`はAXis，`v`はVertical，`line`はLINEのことを表している。
# * 横線の場合
#     ```
#     ax_.axhline(＜縦軸の値＞)
#     ```
#     ここで`axhline`の`ax`はAXis，`h`はHorizontal，`line`はLINEのことを表している。
# 
# ここで`ax_`は`.plot()`で返された「軸」のことである。
# 
# `Y`のヒストグラムを使ってプロットしてみよう。

# In[45]:


ax_ = df1['Y'].plot(kind='hist', alpha=0.1)
ax_.axvline(0)
ax_.axhline(10)
pass


# **＜基本的な引数＞**
# 
# 様々な引数があり図に「飾り付け」をすることができる。詳しくは[このリンク](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html)と[このリンク](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html)を参照することにして，ここでは基本的な引数だけを紹介する。
# * `ymin`：`axvline`の縦軸における最小値（`0`~`1`の値; デフォルト`0`）
# * `ymax`：`axvline`の縦軸における最大値（`0`~`1`の値; デフォルト`1`）
# * `xmin`：`axhline`の横軸における最小値（`0`~`1`の値; デフォルト`0`）
# * `xmax`：`axhline`の横軸における最大値（`0`~`1`の値; デフォルト`1`）
# * `linestyle`：線のスタイル（リストにして列の順番で指定する;`-``--``-.``:`）
# * `linewidth` or `lw`：線の幅
# * `color`：色（リストにして列の順番で指定する; [参照サイト](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)）
#     * `r`は赤
#     * `k`は黒
#     * `g`はグリーン
# * `alpha`：透明度（`0`から`1.0`; デフォルトは`1`）

# 引数を指定してプロットしてみる。

# In[46]:


ax_ = df1['Y'].plot(kind='hist', alpha=0.1)
ax_.axvline(0,
            ymin=0.3,
            ymax=0.95,
            linestyle=':',
            linewidth=5,
            color='g',
            alpha=0.8)
ax_.axhline(10,
            xmin=0.05,
            xmax=0.7,
            linestyle='-.',
            linewidth=3,
            color='k',
            alpha=0.5)
pass


# 最後に上のヒストグラムとカーネル密度推定プロットに縦線を加えてみよう。

# In[47]:


ax_ = df1['X'].plot(kind='hist',
                    density=True,
                    label='Xのヒストグラム',
                    legend=True)
df1['X'].plot(kind='kde',
              ax=ax_,
              label='XのKDE',
              legend=True)
ax_.axvline(0, color='red')
pass


# ### 棒グラフ

# (sec:5-bar)=
# ### 棒グラフ

# まず次のコードでデータを準備しよう。

# In[48]:


df2 = pd.DataFrame({'country':['A','B','C'],
                    'gdp':[100,90,110],
                    'con':[50,60,55],
                    'inv':[15,10,20],
                    'gov':[10,5,30],
                    'netex':[25,15,5]})


# ３国のGDPとその構成要素からなる`DataFrame`である。
# * `country`：国
# * `gdp`：GDP
# * `con`：消費
# * `inv`：投資
# * `gov`：政府支出
# * `netex`：純輸出
# 
# この`DataFrame`を使って棒グラフの作成方法を説明するが，次の構文となる。
# ```
# df1.plot(＜横軸の列ラベル＞, ＜縦軸の列ラベル＞, kind='bar')
# ```
# まずA国の`gdp`の棒グラフを表示してみよう。

# In[49]:


df2.plot('country', 'gdp', kind='bar')
pass


# 複数の棒（データ）を並べたい場合もあるだろう。その場合は`＜縦軸の列ラベル＞`にリストとして指定すれば表示できる。

# In[50]:


df2.plot('country', ['gdp','con'], kind='bar')
pass


# **＜基本的な引数＞**
# 
# 詳しい引数についての説明は[このリンク](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html)を参照することにして，ここでは基本的な引数だけを紹介する。
# * `color`：色（リストにして列の順番で指定する; [参照サイト](https://matplotlib.org/3.1.0/gallery/color/named_colors.html)）
#     * `r`又は`red`：赤
#     * `k`又は`black`：黒
#     * `g`又は`green`：グリーン
# * `stacked`：（ブール型;デフォルトは`False`)
#     * 複数データを使う場合に棒を積み上げるかどうかを指定
# * `fontsize`：横軸・縦軸の数字のフォントサイズの設定
# * `figsize`：図の大きさ
#     * `figsize=(キャンバスの横幅、キャンバスの縦の長さ)`
# * `legend`：凡例の表示を指定
#     * `DataFrame`の場合はデフォルトは`True`
# * `label`：凡例の表現を指定
# * `grid`：グリッド表示（ブール型;デフォルトは`False`)
# * `rot`(rotationの略)：横軸の変数の表示の角度（デフォルトは`90`）
# * `subplots`：複数の図をプロットする（詳細はライン・プロットを参照）
# * `ax`：プロットする「軸」を指定する。
# 
# これらの引数を使いプロットしてみよう。

# In[51]:


df2.plot('country', ['con','inv','gov','netex'], kind='bar',
         color=['red','black','green','orange'],
         stacked=True,
         fontsize=20,
         figsize=(8,4),
#          legend=False       
         label=['消費','投資','政府支出','純輸出'],
         grid=True,
         rot=0
        )
pass


# 次に，ライン・プロットを追加する例を考えてみよう。`df2`には列`gdp`があり，それを表すライン・プロットを重ねることにしよう。

# In[52]:


ax_ = df2.plot('country', ['con','inv','gov','netex'],
         kind='bar',
         stacked=True,
         fontsize=15,
         label=['消費','投資','政府支出','純輸出'],
         rot=0)

df2['gdp'].plot(color='black',      # ライン・プロット (Series)
                      marker='o',
                      legend=True,
                      label='国内総生産',
                      ax=ax_)       # Seriesに有効

ax_.set_title('３カ国のGDPと構成要素', size=20)
ax_.set_xlabel('国', size=15)
ax_.set_ylabel('単位：億米ドル', size=15)
pass


# 棒の高さとGDPのマーカーの高さは同じであることがわかる。このコードでは次の点に注意する必要がある。`gdp`を`Series`として抽出し，メソッド`plot()`を使っていることである。これにより，凡例の表記を自由に変更できることになる。
