from requests import get
import pyrebase
from bs4 import BeautifulSoup



# for simple mcqs
# code.....
def for_simple(contentent,Focus_keyword):
    questionns=0
    questions=[]
    Heading_For_Simple_Mcqs='<h2>Questions For '+Focus_keyword+'</h2>' # Question with h3 tag
    while True:
        code=questionns+6
        
        s=contentent[questionns:code]
        
        if len(contentent[questionns:code]) == 0:
            break
        else:
            questionns=code+1
            Question=s[0]
            option_A=s[1]
            option_B=s[2]
            option_C=s[3]
            option_D=s[4]
            Correct_option=s[5] # correct option
            questions.append(f'<br> <h3>{Question}</h3><p><b>(A)</b> {option_A}<br/><b>(B)</b> {option_B}<br/><b>(C)</b> {option_C}<br/><b>(D)</b> {option_D}<br/></p><button class="questionnsxr{questionns}" onclick="me(\'{Correct_option}\',\'questionnsxr{questionns}\')" style="border: none; background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);">Click Me </button><br/>')
    return Heading_For_Simple_Mcqs+''.join(questions)

# for case based mcqs
# code.....
def for_case_based(contentent,Focus_keyword):
    questionns=0
    questions=[]
    Heading_For_Simple_Mcqs='<h2>Case Based Questions For '+Focus_keyword+'</h2>' # Question with h3 tag
    while True:
        code=questionns+7
        
        s=contentent[questionns:code]
        
        if len(contentent[questionns:code]) == 0:
            break
        else:
            questionns=code+1
            Small_paragraph=s[0] # Small paragraph
            Question=s[1] # Question with h3 tag
            option_A=s[2] # options A
            option_B=s[3] # options B
            option_C=s[4] # options C
            option_D=s[5] # options D
            Correct_option=s[6] # correct option
            questions.append(f'<br> <p>{Small_paragraph}</p><h3>{Question}</h3><p><b>(A)</b> {option_A}<br/><b>(B)</b> {option_B}<br/><b>(C)</b> {option_C}<br/><b>(D)</b> {option_D}<br/></p><button class="questionnsx{questionns}" onclick="me(\'{Correct_option}\',\'questionnsxs{questionns}\')" style="border: none; background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);">Click Me </button><br/>')

    return Heading_For_Simple_Mcqs+''.join(questions)

# for image based mcqs
# code.....
def for_image_based(contentent,Focus_Related_keyword,Focus_keyword):
    questionns=0
    Heading_For_Simple_Mcqs='<h2>Image Based Questions For '+Focus_keyword+'</h2>' # Question with h3 tag
    questions=[]
    while True:
        code=questionns+7

        s=contentent[questionns:code]
        if len(contentent[questionns:code]) == 0:
            break
        else:
            questionns=code+1
            Image_link=s[0]# Image_link
            Question=s[1]# Question with h3 tag
            option_A=s[2]# options A
            option_B=s[3]# options B
            option_C=s[4]# options C
            option_D=s[5]# options D
            Correct_option=s[6]# correct option
            questions.append(f'<br><img src="{Image_link}" alt="{Focus_Related_keyword}"><h3>{Question}</h3><p><b>(A)</b> {option_A}<br/><b>(B)</b> {option_B}<br/><b>(C)</b> {option_C}<br/><b>(D)</b> {option_D}<br/></p><button class="questionnsx{questionns}" onclick="me(\'{Correct_option}\',\'questionnsx{questionns}\')" style="border: none; background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);">Click Me </button><br/>')
    
    return Heading_For_Simple_Mcqs+''.join(questions)


# Some Other Content For Mcqs
def full_bhi_content(extra_contentent,contentent,simple,case,imagebased,image_link):
    Focus_keyword=extra_contentent[0]
    Focus_Related_keyword=extra_contentent[1]
    Short_Description=extra_contentent[2]
    Final_Words=extra_contentent[3]
    jscode="<script>function me(me,c){document.querySelector('.'+c).innerHTML='Your Correct Answer is ('+me+')'}</script>"
    rr=get(extra_contentent[4]).text
    soup = BeautifulSoup(rr, 'html.parser')
    Internal_link=f'<p><b>Read Also</b> :<a href="{extra_contentent[4]}">{soup.title.text}</a></p>'
    if simple=='on':
        quiz_code=for_simple(contentent,Focus_keyword)
    elif case=='on':
        quiz_code=for_case_based(contentent,Focus_keyword)
    elif imagebased=='on':
        quiz_code=for_image_based(contentent,Focus_Related_keyword,Focus_keyword)
    
    Full_content=f'<img src="{image_link}" alt="{Focus_Related_keyword}"><br/><b>{Focus_keyword}</b> :{Short_Description}<br/>{quiz_code}<br/><h2> Final Words :</h2><p>{Final_Words}</p><br/>{Internal_link}<br>{jscode}'
    return Full_content
