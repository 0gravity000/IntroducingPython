# 7.1.2.1 %を使った古いスタイル
n = 42
f = 7.03
s = 'string cheese'

'{} {} {}'.format(n, f, s)

'{2} {0} {1}'.format(n, f, s)

'{n} {f} {s}'.format(n=42, f=7.03, s='string cheese')

d = {'n': 42, 'f': 7.03, 's': 'string cheese'}

'{0[n]} {0[f] {0[s]} {1}}'.format{d, 'other'}

'{0:d} {1:f} {2:s}'.format(n, f, s)

'{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese')

'{0:10d} {1:10f} {2:10s}'.format(n, f, s)

'{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s)

'{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s)

'{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s)

# エラー 整数のこの形式は使えない
'{0:>10.4d} {1:>10.4f} {2:>10.4s}'.format(n, f, s)

'{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s)

# バインディング
# 出力フィールドの隙間をスペース以外の文字で埋めたい場合
'{0:!^20s}'.format('BIG SALE')