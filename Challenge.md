## Inventory Management System

### Build a simple inventory management system that allows a user to perform the following actions:

- Add a new product to the inventory with details such as name, price, quantity, and category.
- Update the details of an existing product.
- Delete a product from the inventory.
- View a list of all products, with the option to filter by category or search by name.
- Calculate the total value of the inventory (sum of price * quantity for all products).

### Requirements:

- Use an in-memory database or local storage to persist the inventory data (if using a web app).
- Create a RESTful API (if back-end focused) or a simple front-end UI to interact with the inventory.

### Tech Stack Ideas:

- Frontend: Vue.js, React, or plain HTML/JS with a lightweight CSS framework like Tailwind or Bootstrap.
- Backend: Node.js with Express, PHP with Laravel, or Python with Flask/Django.
- Database: In-memory (e.g., JavaScript object, SQLite, or IndexedDB for a web app).

### Extra Credit:

- Add user authentication to protect the system (e.g., basic login/logout functionality).
- Implement a feature to export the inventory data as a CSV file.
- Add unit tests for the core functionality.