# Project Requirements

## **Vision**

- This project aspires to provide ease of access to vital COVID related knowledge
when it is needed, with reliability, authenticity and universality being the main
principals of operation of this app. Moreover, the driving force behind this
project was and will always be the passion of developing team it for **equality
and fairness of knowledge**, along with their strong belief that Good health and
well-being are fundamental human rights that should never be compromised or
monetized for any reason.
- With all this in mind, we hope to soften the impact of COVID-19 and possible
similar problems on the people most affected by
it; _those on the front lines and the less fortunate_.

## Scope (In/Out)

- **IN: What will this app product do?**
- This app will provide information to users about Corona Virus
  cases, deaths and directly related pieces of information about the pandemic.
  - This app will provide `.csv.` file containing information about the
  Corona Virus pandmic.
  - The web app will provide a visualization of the data, in order to help
  the user understand the information provided to him in a better way.
- **Out: What will this app product not do?**
  - This application will not provide a PDF file to the user.
  - This application will never allow the user add or modify any of the data we provide.

- Minimum Viable Product
  - What will y this pp MVP functionality be?
    - give to the user the recommended report to deal with any Feature pandemic
  - What are y this pp stretch goals?
    - train the app to be able to predict the future pandemic and give us the
    solution before that heaped
- Stretch
  - What stretch goals are you going to aim for?
    - make the app as AI system.
    - Create a data model to help predict similar situations/events based on
    hisorical data.

- Functional Requirements
  - the use can interact with the GUI.
  - the user can enter a country name.
  - the use can download the data as Json , Html or csv.
  - the use can see the data visualization.
  - the user can receive a notification from the app.
  - the user can see the detailing report.

- Data Flow
  - The app will start at home/welcom screen when the user opens the app.
  - Then they will chooses a _country/region_.
  - They will click on the next.
  - The user then will have the choice of doing one or more of the following:
    - Download: Download a **`.csv`** file containing a table with the info
    viewed within the app concerning the chosen region/country.
    - Visualize: Show a visualization of the viewed data with the option to
    download as an image.
    - Show report: View a short status report of the health situation in the
    chosen country/region.
  - Once chosen, an option will alert the user to the completion of their choice.
  - Terminate: The app will terminate normally whenever the user closes the app window.

- Non-Functional Requirements
  - **Testability**
    - This app app should be able to check the country name and show error if
    it was uncorrected.
    - The app should be able to give the right report to the user.
  - **Reusability**
    - This app app will implement by _SOLID principles_ so every thing will be
    a Functional component.
    - Functions will be reusable, and might be used/called multiple times if
    the need arises.
