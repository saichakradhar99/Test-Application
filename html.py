# Python code to create a basic HTML webpage

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        p {
            margin-bottom: 20px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Sample Webpage</h1>
        <p>This is a simple HTML webpage created using Python.</p>
        <p>Feel free to modify and enhance it!</p>
    </div>
</body>
</html>
"""

# Write HTML content to a file
with open("sample_webpage.html", "w") as file:
    file.write(html_content)

print("Sample webpage created successfully as 'sample_webpage.html'")
