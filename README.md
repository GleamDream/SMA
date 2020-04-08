# Simple Moving Average
Simple Moving Average by numpy.convolve and recursion
単純移動平均(Simple Moving Average)を算出する

# DEMO|Usage
関数moving_average(x, length)
x : 配列(listでもndarrayでも動作確認済み)
length : 平均をとる長さ(int)

returns : 単純移動平均をとった配列(ndarray)

"""
from ma import moving_average

x = [i for i in range(49)]
mv = moving_average(mv, 7)
print(mv)
"""

# Features
通常，numpyのconvolveで移動平均をとるときは，
"""
ave_array = numpy.ones(length) / float(length)
conv_x = numpy.convolve(x, ave_array)
"""
とし，畳み込まれる配列xとnumpy.ones/lengthの畳み込みとなる。
しかし，numpy.convolveで指定できるmode(初期値'full', 'valid', 'same')のどれをとっても
xだけで(ゼロパディングせずに)平均をとったものは無い。
mode=full(デフォルト)の場合，xからはみ出して畳み込みを行う範囲においてゼロパディングして平均をとる。
そのため，返ってくる配列の長さは平均をとる長さ分だけ長くなって返ってくる。
それに対してmode=sameであれば長くなった部分はカットされて返ってくるし，
mode=validはゼロパディングせず，畳み込みが行えない範囲は何もしないため，
返ってくる配列のサイズは，xよりも 平均をとる長さ分だけ短くなって返ってくる。

例) xが64の長さ|平均をとる長さを8 としたときの返ってくる配列の長さ:
mode = full  : 64 + 8 = 72
mode = same  : 64
mode = valid : 64 - 8 = 56

## グラフとして描画する際にとてつもなく厄介かつ美しくない

そこで，xの平均をとることにおいて，ゼロパディングせずに
平均をとる範囲を狭めていきながら配列の端まで平均をとることにした。

# Requirement
* numpy 1.12.1

# Note
配列xの長さが偶数の場合，配列の最後は演算の対象外。
平均をとる長さlが偶数の場合，-1して奇数で演算。

# Author
* 作成者 : Hiromu Ikemura
* 所属 : N.I.T., Okinawa College
* E-mail : ac194601(at)edu.okinawa-ct.ac.jp

# License
"SMA" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License)
