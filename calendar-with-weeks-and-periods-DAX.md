## Calendar with weeks and 4-week periods (DAX)

Defines a calculated calendar table with weeks and 4-week periods:

    Calendar = 
    VAR BaseCalendar =
        CALENDAR (
            DATE ( 2020, 1, 1 ),
            DATE ( 2020, 12, 31 )
        )
    VAR DateToday = TODAY()
    RETURN
        GENERATE (
            BaseCalendar,
            VAR BaseDate = [Date]
            VAR YearDate =
                YEAR ( BaseDate )
            VAR MonthNumber =
                MONTH ( BaseDate )
            VAR WeekNumber =
                WEEKNUM ( BaseDate, 21 ) // iso week number
            VAR WeekIndex =
                INT ( ( BaseDate - 2 ) / 7 ) // sequential week number
            VAR YearNumber =
                YEAR ( BaseDate + ( 3 - WEEKDAY ( BaseDate, 3 ) ) ) // goes with week number
            VAR PeriodNumber =
                ROUNDUP ( WeekNumber / 4, 0 ) // number of the 4-week period
            RETURN
                ROW (
                    "Datum", BaseDate,
                    "Year", YearDate,
                    "Month", FORMAT ( BaseDate, "mmmm" ),
                    "Month no", MonthNumber,
                    "Year month", FORMAT ( BaseDate, "yyyymm" ),
    
                    "Period", "P" & FORMAT ( PeriodNumber, "00" ) & " " & YearNumber,
                    "Period no", PeriodNumber,
                    "Period index",  ROUNDUP ( WeekIndex / 4, 0 ),
    
                    "Week", YearNumber & "-W" & FORMAT ( WeekNumber, "00" ),
                    "Week no", WeekNumber,
                    "Week index", WeekIndex
                )
        )