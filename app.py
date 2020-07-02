import streamlit as st
import json
import requests
import matplotlib.pyplot as plt
import numpy as np

URI = 'http://32c6825dc4dd.ngrok.io/'

st.title('NN visualizer')
st.sidebar.markdown('## Input Image')

if st.button('Get random prediction'):
    response = request.post(URI,data={})
    response=json.loads(response.text)
    preds = response.get('prediction')
    image= response.get('image')
    iamge = np.reshape(image,(28*28))
    
    st.sidebar.image(image,width=150)
    for layer,p in enumerate(preds):
        numbers = np.squeeze(np.array(p))
        plt.figure(figsize=(32,4))
        if layer == 2 :
            row=1
            col=10
        else:
            row=2
            col =16
        for i , number in enumerate(numbers):
            plt.subplot(row,col,i+1)
            plt.imshow(number*np.ones((8,8,4)).astype('float32'))
            pt.xticks([])
            plt.yticks([])
            if layer == 2:
                plt.xlabel(str(i),fontsize=40)
        plt.subplots_adjust(wspace=0.05,hspace=0.05)
        plt.tight_layout()
        st.test('Layer{}'.foramt(i+1))
        st.pyplot()
