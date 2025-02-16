# Data Analysis Toolkit 🎯

Hey! 👋 I made this Python toolkit to make data analysis easier for everyone. It handles CSV/JSON files and creates some neat visualizations. I mainly built it for my own projects but figured others might find it useful too!

## What it does 

- Reads data from CSV & JSON files (might add Excel support later)
- Creates cool visualizations (bar charts, scatter plots etc)
- Generates basic stats like mean, median etc
- Saves everything as nice reports
- Works with both numerical and categorical data

## Getting Started

First, clone this repo:

git clone https://github.com/your-username/data-analysis-tools.git
cd data-analysis-tools

Install the stuff you need:

pip install -r requirements.txt

## How to Use It
Here's a quick example:

from data_analyzer import DataAnalyzer

# Load your data
analyzer = DataAnalyzer('sales_data.csv')  # works with JSON too!

# Get some basic stats
stats = analyzer.generate_summary_statistics()

# Make a nice bar chart
analyzer.create_visualization('bar', 'product_category')
plt.savefig('categories.png')

# Or a scatter plot
analyzer.create_visualization('scatter', 'price', 'sales', 'Price vs Sales')
plt.savefig('price_vs_sales.png')



## Known Issues 🐛

Sometimes the plots look a bit weird with really long category names
Haven't tested it with huge datasets yet
The JSON output could be prettier

## Contributing
Found a bug? Want to add something cool? Feel free to:

## Fork it
Create your feature branch (git checkout -b cool-new-feature)
Commit your changes (git commit -am 'Added something awesome')
Push to the branch (git push origin cool-new-feature)
Make a Pull Request!

# Do whatever you want with it! Just don't blame me if something breaks 😅

PS: If this helped you, stars ⭐ are always appreciated!
