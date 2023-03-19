def main():
    groceries = []
    while True:
        try:
            grocery = input("Enter your list: ").upper()
            groceries.append(grocery)

        except ValueError:
            pass
        except KeyboardInterrupt:
            final_groceries = {g: groceries.count(g) for g in groceries}
            for g in final_groceries:
                print(final_groceries[g],g)
            break
                
                




main()