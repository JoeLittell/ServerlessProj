def sample_classify_text(text_content):
    """
    Classifying Content in a String

    Args:
      text_content The text content to analyze. Must include at least 20 words.
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    response = client.classify_text(document)
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(u"Category name: {}".format(category.name))
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(u"Confidence: {}".format(category.confidence))

def Download_Print(request):
    """Responds to a HTTP request in a JSON format.
    Reads a .txt file using a URL
    Args:
        request: a request with a JSON format {"url":"[any URL.txt]"}.
    Returns:
        file : (str) The text content
    """
    import urllib.request

    request_json = request.get_json()
    if request_json and 'url' in request_json:
        try:
            file = urllib.request.urlopen(request_json['url'])
            file = file.read()
            inform = sample_classify_text(file)
            inform = inform + f'\nOriginal text:\n{file}\n'
            return inform
        except:
            return 'Reading URL failed. Please check the URL.'
    else:
        return 'Query failed.\nPlease submit a query with the following format: {"url":"[A URL ended with .txt]"}'