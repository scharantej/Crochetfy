## Flask Application Design for Handmade Crochet Animals Website

### HTML Files
- **home.html:** This file will serve as the landing page of the website, showcasing the available crochet animals, their descriptions, and their prices.
- **about.html:** This file will provide information about the creator, their inspiration, and the handmade nature of the animals.
- **contact.html:** This file will enable customers to get in touch with the creator by providing a form for inquiries or orders.

### Routes
- **@app.route('/')**: This route will render the **home.html** file, displaying the available crochet animals for purchase.
- **@app.route('/about')**: This route will render the **about.html** file, providing information about the creator and the handmade process.
- **@app.route('/contact')**: This route will render the **contact.html** file, allowing visitors to contact the creator through a form.
- **@app.route('/purchase')**: This route will handle the purchase process, receiving customer information and order details before confirming the order. (Implementation details omitted for this design phase.)