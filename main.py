from tabulate import tabulate
from math import sqrt

class Membership:
    
    # inisialisasi data
    data = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }
    
    # init attribute
    def __init__(self, username: str) -> None:
        self.username = username
        
    def show_benefit(self) -> None:
        """
        Method yang digunakan untuk menampilkan benefit yang ada di PacCommerce
        masing - masing tier Membership
        """
        # init headers name
        headers = ["Membership", "Discount", "Benefits"]
        
        # init data
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojol"],
            ["Silver", "8%", "Voucher Makanan"]
        ]
        
        print("Benefit PacCommerce Memberships")
        print("")
        print(tabulate(tables, headers, tablefmt="github"))
        
    def show_requirements(self) -> None:
        """
        Method yang digunakan untuk menampilkan requirements monthly expense dan income
        dari masing - masing tier memberships
        """
        # init headers name
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        
        # init data
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7]
        ]
        
        print("Requirements PacCommerce Memberships")
        print("")
        print(tabulate(tables, headers, tablefmt="github"))
        
    def predict_membership(self, username: str,
                           monthly_expense: float,
                           monthly_income: float) -> None:
        """
        Method yang digunakan untuk memprediksi user masuk ke tier membership apa
        dengan menggunakan metode Euclidean Distance
        
        Parameters
        ----------
        username (str): username dari user
        monthly_expense (float): pengeluaran perbulan dari user dalam format jutaan
        monthly_income (float): pemasukan perbulan dari user dalam format jutaan
        """
        # init parameter data for each tier membership
        parameter_data = [[8, 15], [6, 10], [5, 7]]
        
        result_tmp = []
        
        for idx, _ in enumerate(parameter_data):

            if monthly_expense < monthly_income:

                # implement euclidean distance
                euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                            (monthly_income - parameter_data[idx][1])**2), 2)
                
                result_tmp.append(euclidean_dist)

            else:
                raise Exception("Income harus lebih besar daripada expense")
            
        # store the euclidean distance values to dictionary
        dict_result = {
            "Platinum": result_tmp[0],
            "Gold": result_tmp[1],
            "Silver": result_tmp[2]
        }
        
        print(f"Hasil perhitungan Euclidean Distance dari user {username} adalah {dict_result}")
        
        # get minimum values from result list
        get_min_distance = min(result_tmp)
        
        # iterate to dictionary data
        for key, value in dict_result.items():
            
            # compare with minimum data
            if value == get_min_distance:
                print(key)
                
                # insert predicted data to dict data
                self.data[username] = key
                
    def calculate_price(self, username: str, list_harga: list) -> float:
        """
        Method yang digunakan untuk menghitung total price diberikan membership
        
        Parameters
        ----------
        username (str): username existing user
        list_harga (list): harga belanjaan user
        
        Returns
        -------
        total_price (float): total akhir dari user
        """
        if username in self.data:
            
            # get membership
            membership = self.data.get(username)
            
            # create branching for each membership to get discount
            if membership == "Platinum":
                total_price = sum(list_harga) - (sum(list_harga) * 0.15)
                
                return total_price
            
            elif membership == "Gold":
                total_price = sum(list_harga) - (sum(list_harga) * 0.10)
                
                return total_price
            
            elif membership == "Silver":
                total_price = sum(list_harga) - (sum(list_harga) * 0.08)
                
                return total_price
            
            else:
                raise Exception("Membership belum terimplementasi")
                
        else:
            raise Exception("Member masih belum ada di Database")

# init object
user_1 = Membership(username = "Shandy")

# check username
print(user_1.username)

# predict membership
user_1.predict_membership(username = "Shandy",
                          monthly_expense = 7,
                          monthly_income = 5)

print(user_1.data)