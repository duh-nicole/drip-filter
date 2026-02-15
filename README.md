💖 Drip-Filter Data Filter

A robust, object-oriented Python application designed to load, filter, and save user data with flair. Built by SoftStack Studios, this app proves that data management doesn't have to be boring.



## 📸 Demo
![Drip-Filter in Action](dripfilterDEMO.png)



🌈 Features

Object-Oriented Architecture: Uses a dedicated User class with private attributes and property decorators for secure data handling.

Dynamic Filtering: Implements getattr for flexible searching across various user attributes (ID, Name, Age, City, Phone).

Drunk-Proof Input Handling: Comprehensive try/except blocks and input validation to handle "ghosts in the machine" without crashing.

Partial Match Search: High-end search logic allows users to find data using fragments (like area codes).

Aesthetic UI: A Scooby-Doo inspired terminal interface featuring emojis and clear feedback.




🛠️ Technical Deep Dive

Encapsulation & Logic Delegation

Unlike basic scripts, Drip-Filter delegates logic to the data model. The User class is responsible for determining if it matches a search criteria, keeping the main.py interface clean and readable.


Scalability
The use of matches_string and matches_range methods means new user attributes can be added to the JSON without needing to rewrite the core filtering engine.





---

## 🚀 How to Run (DIY)

Want to see how I handle the ghosts in the machine? Follow these steps on your own terminal:

1. **Clone the repo:**
   
```bash

git clone [https://github.com/duh-nicole/drip-filter.git](https://github.com/duh-nicole/drip-filter.git)
   
cd drip-filter

```

2. Run the application

```bash

python3 main.py

```

3. Play around
When prompted, enter data.JSON as your source file and start sifting through the data!



📁 File Structure

main.py - The big kahuna; manages the UI and application flow.


user.py - The logic engine; contains the User class and OOP methods.


data.json - Sample dataset for testing.





🍬 Credits
Developed with 💖 by SoftStack Studios
