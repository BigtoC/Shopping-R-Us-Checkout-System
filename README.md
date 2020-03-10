# Shopping-R-Us-Checkout-System

### Environment: 
> Anaconda 3 with Python 3.7

### Run the program:
> In root directory of this project, run `python checkout.py` in command line,  
> or, `right click 'checkout.py' -> Run 'checkout'` in PyCharm  
* Follow instructions after running the program: 
  ```
  Input 'help' to read the instruction. 
  Input 'run' to execute the main function. 
  Input 'end' to exist this program. 
  ```
* 

### Modify Config Data:
* Open `products_config.yaml` with any text editor  
* File structure:
  ```yaml
  Products:
    [SKU]:
      name: [Name]
      price: [Price]
    ...
  Specials:
    - [Specials Rule]
    - [Specials Rule]
    ...
  ```
* Contents inside brackets `[]` are modifiable, with some conditions:
  1. [Price] must be numbers
  2. Follow the format of current [Specials Rule]
  3. For any non-digit attribute, quotes must be used (either single or double quotes)
* Explain the format of [Specials Rule]:
  1. `"3 atv = 2 atv"` : 3 for 2 deal on Apple TVs
  2. `"4 ipd = $499.99"` : the price of iPad will drop to $499.99 each, if someone buys more than 4
  3. `"1 mbp > 1 vga"` : a free VGA adapter free of charge with every MacBook Pro sold  
 
   

