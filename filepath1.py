# import streamlit as st
# #tab1,tab2,tab3=st.tabs("Home","Contact","Settings")
# st.title("Images")
# col1,col2,col3=st.columns(3)
# with col1:
#     with st.popover("Info1"):
#         c1, c2 = st.columns(2)
#         with c1:
#             st.use_container_width=True,
#             st.image(
#                 "https://tse2.mm.bing.net/th/id/OIP.eqjWHgIQbpOMrjYF9D6xiwHaE7?pid=Api&P=0&h=180",
#                 caption="Cat",
               
#             )
#         with c2:
#             st.use_container_width=True,
#             st.image(
#                 "https://tse2.mm.bing.net/th/id/OIP.3ASJSRy03PAtNYOTM-RQwgHaFj?pid=Api&P=0&h=180",
#                 caption="Cats",
                
#             )
# with col2:
#     with st.popover("Info2"):
        
#         c1, c2 = st.columns(2)
#         with c1:
#             st.use_container_width=True,
#             st.image(
#                 "https://tse2.mm.bing.net/th/id/OIP.HkoEj5uMTaX2FGlUUuHUmwHaEy?pid=Api&P=0&h=180",
#                 caption="Dog",
                
#             )
#         with c2:
#             st.use_container_width=True,
#             st.image(
#                 "https://tse3.mm.bing.net/th/id/OIP.YfrOQrCNbEIxTLv41GxELQHaEL?pid=Api&P=0&h=180",
#                 caption="Dogs",
                
#             )

# with col3:
#     with st.popover("Info3"):
       
#         c1, c2 = st.columns(2)
#         with c1:
#             st.use_container_width=True
#             st.image(
#                 "https://tse1.mm.bing.net/th/id/OIP.Rr-dqE4JjaQ2VFN7P4JqswHaEo?pid=Api&P=0&h=180",
#                 caption="Peacock",
                
#             )
#         with c2:
#             st.use_container_width=True,
#             st.image(
#                 "https://tse4.mm.bing.net/th/id/OIP.XFC4Dh-I9uJmYES9ecd6XQHaEZ?pid=Api&P=0&h=180",
#                 caption="Duckling",
                
#             )
# st.divider()
# bt=st.sidebar.title("Select Age Category")
# s1=st.sidebar.selectbox("Choose Projects",["Select","WeatherPrediction","Random Code Generator","Student Form","Registration Form"])

# if bt:
#     option=st.sidebar.radio(
#         "choose one: ",
#         [
#             "select",
#              "category A(Age 0-25)",
#              "category A(Age 26-50)",
#              "category A(Age 51-75)",
#              "category A(Age 76-100)",
#         ]
#     )
#     data = [
#         # 1–25
#         {"name": "Aarav", "age": 18, "gender": "Male", "age_group": "1-25"},
#         {"name": "Priya", "age": 22, "gender": "Female", "age_group": "1-25"},
#         {"name": "Rahul", "age": 24, "gender": "Male", "age_group": "1-25"},
#         {"name": "Sneha", "age": 19, "gender": "Female", "age_group": "1-25"},
#         {"name": "Kiran", "age": 25, "gender": "Male", "age_group": "1-25"},

#         # 26–50
#         {"name": "Vikram", "age": 30, "gender": "Male", "age_group": "26-50"},
#         {"name": "Meera", "age": 35, "gender": "Female", "age_group": "26-50"},
#         {"name": "Raj", "age": 40, "gender": "Male", "age_group": "26-50"},
#         {"name": "Pooja", "age": 45, "gender": "Female", "age_group": "26-50"},
#         {"name": "Amit", "age": 50, "gender": "Male", "age_group": "26-50"},

#         # 51–75
#         {"name": "Karthik", "age": 55, "gender": "Male", "age_group": "51-75"},
#         {"name": "Anjali", "age": 60, "gender": "Female", "age_group": "51-75"},
#         {"name": "Rajesh", "age": 65, "gender": "Male", "age_group": "51-75"},
#         {"name": "Lakshmi", "age": 70, "gender": "Female", "age_group": "51-75"},
#         {"name": "Sundar", "age": 75, "gender": "Male", "age_group": "51-75"},

#         # 76–100
#         {"name": "Suresh", "age": 80, "gender": "Male", "age_group": "76-100"},
#         {"name": "Kamala", "age": 85, "gender": "Female", "age_group": "76-100"},
#         {"name": "Mohan", "age": 90, "gender": "Male", "age_group": "76-100"},
#         {"name": "Leela", "age": 95, "gender": "Female", "age_group": "76-100"},
#         {"name": "Raman", "age": 100, "gender": "Male", "age_group": "76-100"},
#     ]
#     def Filter_data(min_age,max_age):
#         result=[]
#         for person in data:
#             if person["age"]>=min_age and person["age"]<=max_age:
#                 result.append(person)
#         return result        

#     if option == "Category A (Age 0-25)":
#         st.subheader("👶 Category A: Age 0–25")
#         st.table(Filter_data(0, 25))

#     elif option == "Category B (Age 26-50)":
#         st.subheader("🧑 Category B: Age 26–50")
#         st.table(Filter_data(26, 50))

#     elif option == "Category C (Age 51-75)":
#         st.subheader("👵 Category C: Age 51–75")
#         st.table(Filter_data(51, 75))

#     elif option == "Category D (Age 76-100)":
#         st.subheader("🎂 Category D: Age 76–100")
#         st.table(Filter_data(76, 100))
# elif s1:
#     if s1=="WeatherPrediction":
#         st.title("Weather Prediction")
#         st.write('''
#                 **Description:**
#                 The Smart Weather App provides real-time weather updates based on city name.  
#                 It uses the OpenWeather API to show temperature, humidity, and predictions 
#                 with personalized suggestions.''')
#         st.write("https://weatherprediction-8waijgitrzy9mh8s6lh5s5.streamlit.app/")
#     elif s1=="Random Code Generator":
#         st.title("Random Code Genarator")
#         st.write('''
#                 **Description:**
#                 Built using Streamlit, the app generates two random lines of Python code and
#                 displays them instantly on the screen. It’s useful for quick learning, debugging
#                 practice, or even coding inspiration. With a clean interface and real-time 
#                 generation, it makes exploring programming concepts both engaging and effortless.''')
#         st.write("https://randomcodegen-uvyuyudbagwgk6ktewhuuf.streamlit.app/") 
#     elif s1=="Student Form":
#             st.write("Student Form")
#             st.write('''
#                 **Description:**
#                 I created a Student Registration Form using the Streamlit module that collects 
#                 details like First Name, Last Name, Email, and Phone Number through a simple interface. 
#                 After submission, the entered information is displayed in a table format, making it 
#                 easy to view and verify the student details.
#                 ''')
#             st.write("https://studentsdetails-htegejejgsh6w5ygxkstmd.streamlit.app/") 
#     elif s1=="Registration Form":
#         st.write("Introduction about Modules")
#         st.write('''
#                 **Description**
#                 The JSON module in Python is used to handle data in JSON format, allowing easy 
#                 conversion between Python objects and JSON strings. The Requests module helps 
#                 in sending HTTP requests to web servers, making it simple to fetch, send, or 
#                 interact with APIs for real-time data exchange.
#                 ''')
#         st.write("https://new-registerapp-bkdu4hbc4ewfkqepjv3gnm.streamlit.app/")




# #"Random Code Generator","Student Form","Registration Form"])


import streamlit as st


st.set_page_config(page_title="Image Dashboard", layout="wide")
if "page" not in st.session_state:
    st.session_state.page = "home"


st.sidebar.title("🔹 Navigation Panel")

nav_choice = st.sidebar.radio(
    "Go to:",
    ["Home", "Age Category", "Projects"]
)


st.session_state.page = nav_choice.lower()


if st.session_state.page == "home":
    st.title("🐾 Animal Image Gallery")
    col1, col2, col3 = st.columns(3)

    with col1:
        with st.popover("Info 1"):
            c1, c2 = st.columns(2)
            with c1:
                st.image(
                    "https://tse2.mm.bing.net/th/id/OIP.eqjWHgIQbpOMrjYF9D6xiwHaE7?pid=Api&P=0&h=180",
                    caption="Cat",
                    use_container_width=True
                )
            with c2:
                st.image(
                    "https://tse2.mm.bing.net/th/id/OIP.3ASJSRy03PAtNYOTM-RQwgHaFj?pid=Api&P=0&h=180",
                    caption="Cats",
                    use_container_width=True
                )

    with col2:
        with st.popover("Info 2"):
            c1, c2 = st.columns(2)
            with c1:
                st.image(
                    "https://tse2.mm.bing.net/th/id/OIP.HkoEj5uMTaX2FGlUUuHUmwHaEy?pid=Api&P=0&h=180",
                    caption="Dog",
                    use_container_width=True
                )
            with c2:
                st.image(
                    "https://tse3.mm.bing.net/th/id/OIP.YfrOQrCNbEIxTLv41GxELQHaEL?pid=Api&P=0&h=180",
                    caption="Dogs",
                    use_container_width=True
                )

    with col3:
        with st.popover("Info 3"):
            c1, c2 = st.columns(2)
            with c1:
                st.image(
                    "https://tse1.mm.bing.net/th/id/OIP.Rr-dqE4JjaQ2VFN7P4JqswHaEo?pid=Api&P=0&h=180",
                    caption="Peacock",
                    use_container_width=True
                )
            with c2:
                st.image(
                    "https://tse4.mm.bing.net/th/id/OIP.XFC4Dh-I9uJmYES9ecd6XQHaEZ?pid=Api&P=0&h=180",
                    caption="Duckling",
                    use_container_width=True
                )


elif st.session_state.page == "age category":
    st.title("👨‍👩‍👧 Age Category Details")

    data = [
        {"name": "Aarav", "age": 18, "gender": "Male"},
        {"name": "Priya", "age": 22, "gender": "Female"},
        {"name": "Rahul", "age": 24, "gender": "Male"},
        {"name": "Sneha", "age": 19, "gender": "Female"},
        {"name": "Kiran", "age": 25, "gender": "Male"},
        {"name": "Vikram", "age": 30, "gender": "Male"},
        {"name": "Meera", "age": 35, "gender": "Female"},
        {"name": "Raj", "age": 40, "gender": "Male"},
        {"name": "Pooja", "age": 45, "gender": "Female"},
        {"name": "Amit", "age": 50, "gender": "Male"},
        {"name": "Karthik", "age": 55, "gender": "Male"},
        {"name": "Anjali", "age": 60, "gender": "Female"},
        {"name": "Rajesh", "age": 65, "gender": "Male"},
        {"name": "Lakshmi", "age": 70, "gender": "Female"},
        {"name": "Sundar", "age": 75, "gender": "Male"},
        {"name": "Suresh", "age": 80, "gender": "Male"},
        {"name": "Kamala", "age": 85, "gender": "Female"},
        {"name": "Mohan", "age": 90, "gender": "Male"},
        {"name": "Leela", "age": 95, "gender": "Female"},
        {"name": "Raman", "age": 100, "gender": "Male"},
    ]

    def filter_data(min_age, max_age):
        return [p for p in data if min_age <= p["age"] <= max_age]

    category = st.radio(
        "Select Age Group:",
        [
            "Category A (Age 0–25)",
            "Category B (Age 26–50)",
            "Category C (Age 51–75)",
            "Category D (Age 76–100)",
        ],
        horizontal=True
    )

    if category == "Category A (Age 0–25)":
        st.subheader("👶 Category A")
        st.table(filter_data(0, 25))

    elif category == "Category B (Age 26–50)":
        st.subheader("🧑 Category B")
        st.table(filter_data(26, 50))

    elif category == "Category C (Age 51–75)":
        st.subheader("👵 Category C")
        st.table(filter_data(51, 75))

    elif category == "Category D (Age 76–100)":
        st.subheader("🎂 Category D")
        st.table(filter_data(76, 100))


elif st.session_state.page == "projects":
    st.title("💻 My Streamlit Projects")

    s1 = st.selectbox(
        "Choose Project:",
        ["Select", "WeatherPrediction", "Random Code Generator", "Student Form", "Registration Form"]
    )

    if s1 == "WeatherPrediction":
        st.subheader("🌤️ Weather Prediction")
        st.write('''
        The Smart Weather App provides real-time weather updates based on city name.  
        It uses the OpenWeather API to show temperature, humidity, and predictions 
        with personalized suggestions.
        ''')
        st.link_button("Open Weather Prediction App", "https://weatherprediction-8waijgitrzy9mh8s6lh5s5.streamlit.app/")

    elif s1 == "Random Code Generator":
        st.subheader("🧠 Random Code Generator")
        st.write('''
        Built using Streamlit, this app generates random lines of Python code instantly.  
        Great for coding practice, debugging, or inspiration!
        ''')
        st.link_button("Open Random Code Generator", "https://randomcodegen-uvyuyudbagwgk6ktewhuuf.streamlit.app/")

    elif s1 == "Student Form":
        st.subheader("🧾 Student Registration Form")
        st.write('''
        Collects student details like Name, Email, and Phone Number, and displays 
        them in a table format after submission.
        ''')
        st.link_button("Open Student Form", "https://studentsdetails-htegejejgsh6w5ygxkstmd.streamlit.app/")

    elif s1 == "Registration Form":
        st.subheader("📘 Module Explanation: JSON & Requests")
        st.write('''
        **JSON module** helps convert between Python objects and JSON strings.  
        **Requests module** helps send HTTP requests and interact with web APIs.
        ''')
        st.link_button("Open Registration Form", "https://new-registerapp-bkdu4hbc4ewfkqepjv3gnm.streamlit.app/")
