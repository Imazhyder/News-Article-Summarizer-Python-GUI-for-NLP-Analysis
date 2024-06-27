#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from textblob import TextBlob
from newspaper import Article


# In[12]:


def summarize():
    # Function to summarize the article from the provided URL
    
    # Get URL from the text entry
    url = utext.get('1.0', "end").strip()

    # Downloading, parsing, and performing natural language processing on the article
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Enabling editing for display fields
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clearing previous content
    title.delete('1.0','end')
    author.delete('1.0','end')
    publication.delete('1.0','end')
    summary.delete('1.0','end')
    sentiment.delete('1.0','end')

    # Inserting new content
    title.insert('1.0', article.title)
    author.insert('1.0', article.authors)
    publication.insert('1.0', article.publish_date)
    summary.insert('1.0', article.summary)

    # Performing sentiment analysis using TextBlob
    analysis = TextBlob(article.text)
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Disabling editing for display fields
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# In[13]:


# Creating the GUI window using tkinter
root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

# Displaying labels and text fields for article information
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1.2, width=100)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1.2, width=100)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publishing Date')
plabel.pack()
publication = tk.Text(root, height=1.2, width=100)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=19, width=130)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()
sentiment = tk.Text(root, height=1.2, width=130)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()
utext = tk.Text(root, height=1, width=130)
utext.pack()

btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

# Starting the GUI event loop
root.mainloop()


# In[ ]:




