def main():
    amount_due = 50
    # is_amount_due = True
    ''' Instead of using flag we can directly check if amount due is 0 or less to stop while loop'''

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        user_coin = int(input("Insert Coin: "))
        
        #validate user denomination 5,10,25
        #valid_coin = lambda coin : coin in [5,10,25]

        '''Here i have removed lambda function because since the lambda function is defined inside the loop, it will
        get initialised for every iteration which is inefficient'''

        if valid_coin(user_coin):
            amount_due -= user_coin

            ''' Removed the amount due check block as we are checking it in the while block'''
            # if amount_due <= 0:
            #     is_amount_due = False

        ''' I have removed else block because incase of invalid coin it will go for next iteration
         so no need to speicfy the else condition. In else block we are explicityly specifying to 
         continue next iteration incase of invalid coin which is not need as when the if condition 
         evaluates to False it will go for next iteration even without else clause'''
        #else:
            #continue

    print(f"Change Owed: {abs(amount_due)}")


def valid_coin(coin):
    return coin in [5,10,25]

main()
