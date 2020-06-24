
## Remove duplicates based on sorted data (M-formula)

Inspired by: [Curbal](https://www.youtube.com/watch?v=rqDdnNxSgHQ&index=22&list=PLDz00l_jz6zzttb28XH8GHZNL6vvpBlkQ)


    let
        Bron = Csv.Document(File.Contents("C:\temp\pc6hnr20190801_gwb_1101.csv"),[Delimiter=";", Columns=5, Encoding=1252, QuoteStyle=QuoteStyle.None]),
        #"Headers met verhoogd niveau" = Table.PromoteHeaders(Bron, [PromoteAllScalars=true]),
        #"Type gewijzigd" = Table.TransformColumnTypes(#"Headers met verhoogd niveau",{{"PC6", type text}, {"Huisnummer", Int64.Type}, {"Buurt2019", Int64.Type}, {"Wijk2019", Int64.Type}, {"Gemeente2019", Int64.Type}}),
        #"Rijen gefilterd" = Table.SelectRows(#"Type gewijzigd", each [PC6] = "1011HB"),
        #"Rijen gegroepeerd" = Table.Group(#"Rijen gefilterd", {"PC6", "Buurt2019"}, {{"Aantal", each Table.RowCount(Table.Distinct(_)), Int64.Type}}),
        #"Rijen gesorteerd" = Table.Sort(#"Rijen gegroepeerd",{{"PC6", Order.Ascending}, {"Aantal", Order.Descending}}),
        #"Buffer table" = Table.Buffer(#"Rijen gesorteerd"),
        #"Dubbele waarden verwijderd" = Table.Distinct(#"Buffer table", {"PC6"})
    in
        #"Dubbele waarden verwijderd"


