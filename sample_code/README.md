# Sample Code for Python Software Carpentry

This directory contains comprehensive sample code that follows the **Programming with Python** curriculum from Software Carpentry. The code demonstrates practical programming concepts using the inflammation data analysis scenario.

## 📁 Directory Structure

```
sample_code/
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── plots/                        # Directory for generated plots
├── 01_python_fundamentals.py     # Episode 1: Variables, data types, basic operations
├── 02_numpy_analysis.py          # Episode 2: Loading and analyzing data with NumPy
├── 03_matplotlib_visualization.py # Episode 3: Creating plots and visualizations
├── 04_lists.py                   # Episode 4: Working with Python lists
├── 05_loops.py                   # Episode 5: Automating tasks with loops
├── 06_multiple_files.py          # Episode 6: Processing multiple data files
├── 07_conditionals.py            # Episode 7: Making decisions with conditionals
├── 08_functions.py               # Episode 8: Creating and using functions
├── 09_errors_exceptions.py       # Episode 9: Handling errors gracefully
├── 10_defensive_programming.py   # Episode 10: Writing robust, reliable code
├── 11_debugging.py               # Episode 11: Debugging techniques and strategies
└── 12_command_line.py            # Episode 12: Creating command-line tools
```

## 🎯 Learning Objectives

Each script demonstrates key programming concepts:

### Episode 1: Python Fundamentals
- Variables and assignment
- Data types (int, float, string, boolean)
- Built-in functions
- Basic calculations and operations

### Episode 2: NumPy Analysis
- Loading CSV data with NumPy
- Array operations and slicing
- Statistical calculations (mean, max, min, std)
- Working with multi-dimensional data

### Episode 3: Matplotlib Visualization
- Creating line plots, scatter plots, bar charts
- Customizing plot appearance
- Creating subplots and complex figures
- Saving plots to files

### Episode 4: Lists
- Creating and modifying lists
- List indexing and slicing
- List methods (append, extend, remove)
- Working with nested lists

### Episode 5: Loops
- For loops and while loops
- Using range() function
- Processing multiple files
- Accumulating results

### Episode 6: Multiple Files
- Using glob to find files
- Processing batches of data
- Error handling in file operations
- Creating summary reports

### Episode 7: Conditionals
- if/elif/else statements
- Comparison and logical operators
- Boolean logic
- Decision-making algorithms

### Episode 8: Functions
- Defining and calling functions
- Parameters and return values
- Default parameters
- Function documentation

### Episode 9: Error Handling
- Understanding error types
- try/except blocks
- Creating custom exceptions
- Graceful error recovery

### Episode 10: Defensive Programming
- Using assertions
- Input validation
- Pre- and post-conditions
- Writing testable code

### Episode 11: Debugging
- Reading error messages
- Using print statements for debugging
- Systematic debugging approaches
- Debugging best practices

### Episode 12: Command-Line Programs
- Using sys.argv and argparse
- Creating Unix-style tools
- Handling different input/output formats
- Pipeline integration

## 🚀 Getting Started

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Required packages** (install with pip):
   ```bash
   pip install -r requirements.txt
   ```

### Installing Dependencies

```bash
# Navigate to the sample_code directory
cd sample_code/

# Install required packages
pip install numpy matplotlib
```

### Running the Examples

Each script can be run independently:

```bash
# Basic examples (no dependencies)
python 01_python_fundamentals.py
python 04_lists.py
python 05_loops.py

# Examples requiring NumPy/Matplotlib
python 02_numpy_analysis.py
python 03_matplotlib_visualization.py

# Advanced examples
python 08_functions.py
python 09_errors_exceptions.py
python 10_defensive_programming.py
```

### Working with Data Files

The scripts expect the inflammation data files to be in the `../data/` directory (relative to the sample_code folder). Make sure you have the CSV files:

- `inflammation-01.csv` through `inflammation-12.csv`
- `small-01.csv`, `small-02.csv`, `small-03.csv`

## 📊 Data Context

All examples use the **arthritis inflammation clinical trial** scenario:

- **Scenario**: Dr. Maverick's inflammation treatment trial
- **Data**: Daily inflammation readings for 60 patients over 40 days
- **Format**: CSV files with patients as rows, days as columns
- **Goal**: Analyze treatment effectiveness

## 🧪 Running Specific Examples

### Basic Data Analysis
```bash
python 02_numpy_analysis.py
```
Demonstrates loading CSV data and calculating statistics.

### Creating Visualizations
```bash
python 03_matplotlib_visualization.py
```
Generates various plots and saves them to the `plots/` directory.

### Processing Multiple Files
```bash
python 06_multiple_files.py
```
Shows how to analyze multiple datasets systematically.

### Command-Line Tool Usage
```bash
python 12_command_line.py
```
Demonstrates building tools that work like Unix commands.

## 🔧 Customizing the Examples

### Modifying Data Paths
If your data files are in a different location, update the file paths in the scripts:

```python
# Change this line in relevant scripts
data = np.loadtxt('data/inflammation-01.csv', delimiter=',')

# To this (example for different path)
data = np.loadtxt('/path/to/your/data/inflammation-01.csv', delimiter=',')
```

### Adjusting Plot Output
To save plots to a different directory:

```python
# Change plot save paths in 03_matplotlib_visualization.py
plt.savefig('your_directory/plot_name.png')
```

## 🐛 Troubleshooting

### Common Issues

1. **ImportError: No module named 'numpy'**
   ```bash
   pip install numpy matplotlib
   ```

2. **FileNotFoundError: 'data/inflammation-01.csv'**
   - Ensure data files are in the correct location
   - Check file paths in the scripts

3. **Permission denied when saving plots**
   - Ensure the `plots/` directory is writable
   - Check file permissions

### Getting Help

- **Read the comments**: Each script has detailed comments explaining the code
- **Check episode documentation**: Refer to the corresponding Software Carpentry lesson
- **Run individual sections**: Comment out parts of the code to focus on specific concepts

## 📚 Learning Path

**Beginner Path:**
1. Start with `01_python_fundamentals.py`
2. Move to `04_lists.py` and `05_loops.py`
3. Try `07_conditionals.py` and `08_functions.py`

**Intermediate Path:**
4. Work through `02_numpy_analysis.py`
5. Explore `06_multiple_files.py`
6. Practice with `09_errors_exceptions.py`

**Advanced Path:**
7. Study `10_defensive_programming.py`
8. Master `11_debugging.py`
9. Build tools with `12_command_line.py`
10. Create visualizations with `03_matplotlib_visualization.py`

## 💡 Tips for Learning

- **Run the code**: Don't just read it - execute each script
- **Modify examples**: Change parameters and see what happens
- **Break things**: Introduce errors to see how they're handled
- **Build incrementally**: Start with simple modifications
- **Read error messages**: They contain valuable learning information

## 🤝 Contributing

If you find issues or have suggestions for improvements:

1. **Check the original lesson**: [Software Carpentry Python Lesson](https://swcarpentry.github.io/python-novice-inflammation/)
2. **Understand the pedagogy**: These examples follow educational best practices
3. **Test your changes**: Ensure examples still work and teach effectively

## 📖 Additional Resources

- **Software Carpentry Python Lesson**: https://swcarpentry.github.io/python-novice-inflammation/
- **Python Documentation**: https://docs.python.org/3/
- **NumPy Documentation**: https://numpy.org/doc/
- **Matplotlib Documentation**: https://matplotlib.org/stable/

## 🏆 Learning Outcomes

After working through these examples, you should be able to:

✅ Write clean, readable Python code  
✅ Analyze tabular data with NumPy  
✅ Create meaningful data visualizations  
✅ Process multiple files systematically  
✅ Handle errors gracefully  
✅ Write reusable functions  
✅ Debug programs effectively  
✅ Create command-line tools  
✅ Apply defensive programming practices  
✅ Follow Python best practices  

---

**Happy Learning!** 🐍📊

Remember: *"The best way to learn programming is to do something useful."* These examples provide practical, real-world programming scenarios that build your skills progressively.