
# DPP Platform

This project is a Django-based Digital Product Passport (DPP) platform. It is designed to manage various types of products, including their manufacturers, importers, dealers, and environmental data.

## Project Structure

- **dpp_platform**: The main Django project directory.
  - **products**: The Django app that contains all the models and views related to products and their data.

## Models

### Manufacturer
Stores information about product manufacturers.

### Product
Represents the products with their unique identifiers, compliance documentation, and user manuals.

### DigitalProductPassport
Stores the digital product passport information.

### Importer
Holds information about importers.

### Dealer
Stores information about dealers who handle the products.

### EnvironmentalData
Contains various environmental metrics associated with the products.

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:
   ```sh
   cd dpp_platform
   ```

3. **Create a virtual environment**:
   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. **Install dependencies**:
   ```sh
   pip install django
   ```

5. **Apply migrations**:
   ```sh
   python manage.py migrate
   ```

6. **Run the development server**:
   ```sh
   python manage.py runserver
   ```

7. **Access the application**:
   Open a web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Admin Interface**: Manage manufacturers, products, digital product passports, importers, dealers, and environmental data through the Django admin interface at `http://127.0.0.1:8000/admin/`.
- **Product Details**: View detailed information about each product, including its environmental data.

## Testing

Run the tests using Django's test framework:

```sh
python manage.py test products
```

## License

This project is licensed under the MIT License.
