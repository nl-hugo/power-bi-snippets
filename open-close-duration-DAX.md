## Reporting the number of started, closed and open cases in a period (DAX)

When reporting the number of sales on a specific day, a relationship between the date table and the order date in the 
sales table will save our day. This will not work however, when we need to report the number of employees in a certain 
month for example or the number of active cases at the end of the year. This pattern introduces a number of measures 
that compute the number of entities started, ended and active in a certain period of time. Note that a period is defined 
by the filter that is applied to the date table.

First, let start with the measure that counts the number of unique cases:

    Number of Cases = DISTINCTCOUNT ( Traject[id] )

Compute the number of cases started in the selected period

    Cases started = 
    VAR FirstVisibleDate = MIN ( Calendar[Date] )
    VAR LastVisibleDate = MAX ( Calendar[Date] )
    RETURN
        CALCULATE ( 
            [Number of Cases],
            Traject[startDate] >= FirstVisibleDate,
            Traject[startDate] <= LastVisibleDate
        )
    
And the number of cases closed in the selected period

    Cases closed = 
    VAR FirstVisibleDate = MIN ( Calendar[Date] )
    VAR LastVisibleDate = MAX ( Calendar[Date] )
    RETURN
        CALCULATE ( 
            [Number of Cases],
            Traject[endDate] >= FirstVisibleDate,
            Traject[endDate] <= LastVisibleDate
        )

Now, the number of cases that are active on the last day of the selected period. These are all the cases that are 
started on or before the last date, but are not closed yet.

    Active cases (EOP) = 
    VAR LastVisibleDate = MAX ( Calendar[Date] )
    RETURN
        CALCULATE ( 
            [Number of Cases],
            Traject[startDate] <= LastVisibleDate,
            Traject[endDate] > LastVisibleDate || ISBLANK ( Traject[endDate] )
        )

And a slight variation to the previous measure: the number of cases that was active at any moment in the given period. 
This includes cases that started after the first date in the periode and closed before the end of the period, which 
would be missed by a measure reporting only on the last day of a period.

    Active cases (IP) = 
    VAR FirstVisibleDate = MIN ( Calendar[Date] )
    VAR LastVisibleDate = MAX ( Calendar[Date] )
    RETURN
        CALCULATE ( 
            [Number of Cases],
            Traject[startDate] <= LastVisibleDate,
            Traject[endDate] >= FirstVisibleDate || ISBLANK ( Traject[endDate] )
        )