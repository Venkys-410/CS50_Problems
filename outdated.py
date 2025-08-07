def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ] 
    while True:
        try:
            user_date = input('Date: ').strip()
            if '/' in user_date:
                date_parts = user_date.split('/')
                if len(date_parts) != 3:
                    raise ValueError()
                
                month,date,year = list(map(int,date_parts))

                if month > 12 or date > 31:
                    raise ValueError()
                print(f'{year}-{month:02}-{date:02}')
                break
            elif ',' in user_date:
                date_parts1 = user_date.split()
                month1 = date_parts1[0].capitalize()
                date1 = int(date_parts1[1].replace(',',''))
                year1 = int(date_parts1[2])

                if not month1 in months or date1 > 31:
                    raise ValueError()
                
                print(f'{year1}-{months.index(month1)+1:02}-{date1:02}')
                break
                
            else:
                raise ValueError()
            

        except (ValueError,TypeError):
            continue
        

        


main()
    