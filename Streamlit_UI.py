import streamlit as st
from BlockchainDataBase.Blockchain import Blockchain
from BlockchainDataBase.Block import Block

#images : https://www.finance-monthly.com/Finance-Monthly/wp-content/uploads/2021/12/iStock-862230824-724x430.jpg
#images: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.tasmeemme.com%2Fen%2Fstore-items%2Fblockchain-technology-background-blue-digital-pattern-bussines-concept-banner-blockchain-vector-concept-illustration-vector-technology-blockchain-background%2F%3Fitem%3D10123671546&psig=AOvVaw0mXOgjMfGDSIdlzOIakQ2-&ust=1670053496733000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOiTmp242vsCFQAAAAAdAAAAABAs
#image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fsearch%3Fk%3Dblack%2Bblockchain&psig=AOvVaw0uI-O-XWKLTi3wm-TZUsdb&ust=1670053764944000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKiHqp252vsCFQAAAAAdAAAAABAF
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.finance-monthly.com/Finance-Monthly/wp-content/uploads/2021/12/iStock-862230824-724x430.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('BG.jpg')


# Title
st.title("Blockchain Transaction Database")

# Header
st.header("Simple Blockchain Based Transaction ledger")

name = st.text_input("Enter your transaction data here", "Type Here ...")
data = name

bc = Blockchain()
bc.add_block(data)
#print(bc.print_blocks())

st.button("Send in the Blockchain Database")

st.write(bc.chain)
st.write(bc.data_base)

status = bc.validate_chain()
if status == True:
    st.header("The Chain is Valid!")
    st.success("Success")

if status == "False":
    st.header("The Chain is Invalid!")


st.write("THE TOTAL NUMBER OF TRANSACTION IN THE CHAIN IS " + str((len(bc.chain))))

with st.sidebar:
    st.title("Blockchain: About")
    st.write("Blockchain.com is a cryptocurrency financial services company. The company began as the first Bitcoin blockchain explorer in 2011 and later created a cryptocurrency wallet that accounted for 28% of bitcoin transactions between 2012 and 2020.")
    # import Image from pillow to open images
    from PIL import Image

    img = Image.open("Cube.png")

    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)

    st.title("Block Height: " + str((len(bc.chain))))

    st.write("The block height is the same as the length of the block, this means it is the number of blocks that are added in the blockchain")

    img = Image.open("Blockchain.png")

    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=250)