
## Create last refresh date (M-formula)

Inspired by: [Chris Webb](https://blog.crossjoin.co.uk/2016/06/03/creating-tables-in-power-bipower-query-m-code-using-table/)

    = #table(type table[LastRefresh=datetime], {{DateTime.LocalNow()}})


