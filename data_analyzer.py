import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import json

class DataAnalyzer:
    """A class to analyze and visualize data from CSV or JSON files."""
    
    def __init__(self, file_path):
        """Initialize the analyzer with a file path."""
        self.file_path = Path(file_path)
        self.data = None
        self.load_data()
    
    def load_data(self):
        """Load data from either CSV or JSON file."""
        if self.file_path.suffix.lower() == '.csv':
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.suffix.lower() == '.json':
            self.data = pd.read_json(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or JSON.")
    
    def generate_summary_statistics(self):
        """Generate basic summary statistics for numerical columns."""
        numeric_columns = self.data.select_dtypes(include=['int64', 'float64']).columns
        summary_stats = {
            'column_stats': {},
            'total_rows': len(self.data)
        }
        
        for column in numeric_columns:
            summary_stats['column_stats'][column] = {
                'mean': self.data[column].mean(),
                'median': self.data[column].median(),
                'std': self.data[column].std(),
                'min': self.data[column].min(),
                'max': self.data[column].max()
            }
        
        return summary_stats
    
    def analyze_categorical_data(self, column_name):
        """Analyze frequency distribution of a categorical column."""
        if column_name not in self.data.columns:
            raise ValueError(f"Column '{column_name}' not found in dataset")
        
        return self.data[column_name].value_counts()
    
    def create_visualization(self, plot_type, x_column, y_column=None, title=None):
        """Create various types of plots based on the data."""
        plt.figure(figsize=(10, 6))
        
        if plot_type == 'bar':
            data = self.analyze_categorical_data(x_column)
            plt.bar(data.index, data.values)
            plt.xticks(rotation=45)
            
        elif plot_type == 'scatter':
            if y_column is None:
                raise ValueError("Scatter plot requires both x and y columns")
            plt.scatter(self.data[x_column], self.data[y_column])
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            
        elif plot_type == 'line':
            plt.plot(self.data[x_column], self.data[y_column] if y_column else self.data.index)
            plt.xlabel(x_column)
            if y_column:
                plt.ylabel(y_column)
                
        elif plot_type == 'histogram':
            plt.hist(self.data[x_column], bins=30)
            plt.xlabel(x_column)
            plt.ylabel('Frequency')
            
        else:
            raise ValueError("Unsupported plot type")
        
        plt.title(title or f"{plot_type.capitalize()} Plot of {x_column}")
        plt.tight_layout()
        return plt

    def save_analysis_report(self, output_path):
        """Save analysis results to a JSON file."""
        summary_stats = self.generate_summary_statistics()
        
        report = {
            'file_analyzed': self.file_path.name,
            'total_rows': summary_stats['total_rows'],
            'columns_analyzed': list(summary_stats['column_stats'].keys()),
            'summary_statistics': summary_stats['column_stats']
        }
        
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=4)

# Example usage
if __name__ == "__main__":
    # Sample data creation for demonstration
    sample_data = {
        'sales': [100, 150, 200, 120, 180, 210, 160, 190, 140, 170],
        'customer_type': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'B'],
        'satisfaction': [4.5, 3.8, 4.2, 3.9, 4.7, 4.1, 3.6, 4.3, 4.0, 4.4]
    }
    
    # Save sample data to CSV
    pd.DataFrame(sample_data).to_csv('sample_data.csv', index=False)
    
    # Initialize analyzer
    analyzer = DataAnalyzer('sample_data.csv')
    
    # Generate and save analysis report
    analyzer.save_analysis_report('analysis_report.json')
    
    # Create various visualizations
    # Bar plot of customer types
    analyzer.create_visualization('bar', 'customer_type', title='Customer Type Distribution')
    plt.savefig('customer_distribution.png')
    
    # Scatter plot of sales vs satisfaction
    analyzer.create_visualization('scatter', 'sales', 'satisfaction', 
                                'Sales vs Customer Satisfaction')
    plt.savefig('sales_satisfaction_scatter.png')
    
    # Histogram of satisfaction scores
    analyzer.create_visualization('histogram', 'satisfaction', 
                                title='Distribution of Satisfaction Scores')
    plt.savefig('satisfaction_histogram.png')
