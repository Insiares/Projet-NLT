from Components.Call_API import call_gpt
from Components.utils_streamlit import variable_session, click_prompt, reset_prompt
import streamlit as st
from time import time
from Database.mongodb import insert_in_database, get_database, close_connection, update_database
from execbox import execbox
import sys
import json
from code_editor import code_editor
import sys
from io import StringIO
import openai
import pandas as pd



#-----------------------------------------------Declare logics----------------------------------------
if 'prompted' not in st.session_state:
    st.session_state.prompted = False

if 'ret_output' not in st.session_state:
    st.session_state.ret_output = "init"
    
if 'clef' not in st.session_state:
    st.session_state.clef = "1"

with st.sidebar:
    st.subheader('Sessions')
    st.button('Debug', on_click=reset_prompt)
    name = st.text_input(label= 'Nom',label_visibility='hidden',placeholder=f"Entrez votre nom", value='Anonyme')

#Declaring a sidebar with session History
with st.sidebar: 
    sessions, client = get_database(name)
    list_session_prompt = [str(y['prompt'][:25]+'...') for y in sessions]
    list_session_prompt.insert(0, 'New_prompt...')
    sidebar_change = False
    selected_option = st.radio('Select Past Prompt', [y for y in list_session_prompt])
                            #    , on_change=onchange_sidebar)
    if selected_option != 'New_prompt...':
        selected_index = list_session_prompt.index(selected_option)
        ret_, nom, prompt_ = variable_session(selected_index, name)
        ret=ret_
        prompt = prompt_
    else:
        ret = None
        prompt = None



def update():
    print(st.session_state.outy)
#-----------------------------------------------//Declare logics//----------------------------------------


#-----------------------------------------------Layout ----------------------------------------

st.title("Prototype Chat_GPT")

# # debug db
# client, collection = connection_mongodb()

# for y in collection.find():
#     st.write(y)


choosen_langage = st.selectbox(
    'Choisissez votre langage',
    ('python', 'JS', 'C'))


Prompt = st.text_area(label= 'prompt',label_visibility='hidden', value=prompt, key=2)
# , on_change= prompt_change)

cols_up1, cols_up2 = st.columns([3,1])

with cols_up2:
    bip = st.button(label="Generate", on_click=click_prompt, disabled=st.session_state.prompted)

#splitting bottom of page
cols_bot1, cols_bot2 = st.columns(2)



if bip:
    heure = time()
    ret = call_gpt(Prompt, choosen_langage)
    duree = round((time() - heure), 2)
    st.write(f" Le résultat a mis {duree} secondes à être généré")
    insert_in_database(Prompt, ret, name)
    sessions, client = get_database(name)
    close_connection(client)



# with cols_bot1:
#     Output = st.text_area(label='AI Output', label_visibility='hidden', value=ret, key='outy', height=200, on_change=update)
    #TO_DO : on_change= update_DB()
# with cols_bot2:
#     st.write('')
#     st.write('')
#     st.markdown(Output)
with cols_up2:
    st.button(label='Prompt Again', on_click=reset_prompt, disabled=not st.session_state.prompted)


def excecuter(retour=ret):
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    try:
        if ret:
            # Exécutez le code
            # execbox(ret)
            exec(retour)
            result_text = new_stdout.getvalue()
            st.write(result_text)

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

    finally:
        # Restaurer
        sys.stdout = old_stdout



with open('Components/custom_buttons.json') as json_button_file_alt:
    custom_buttons_alt = json.load(json_button_file_alt)

# Load Info bar CSS from JSON file
with open('Components/info_bar.json') as json_info_file:
    info_bar = json.load(json_info_file)

# Load Code Editor CSS from file
with open('Components/code_editor_css.scss') as css_file:
    css_text = css_file.read()

# construct component props dictionary (->Code Editor)
comp_props = {"css": css_text, "globalCSS": ":root {\n  --streamlit-dark-font-family: monospace;\n}"}

mode_list = ["abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql", "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "bibtex", "c9search", "c_cpp", "cirru", "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra", "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools", "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl", "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml", "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini", "io", "ion", "jack", "jade", "java", "javascript", "jexl", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia", "kotlin", "latex", "latte", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage", "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mips", "mixal", "mushcode", "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "partiql", "pascal", "perl", "pgsql", "php", "php_laravel_blade", "pig", "plain_text", "powershell", "praat", "prisma", "prolog", "properties", "protobuf", "puppet", "python", "qml", "r", "raku", "razor", "rdoc", "red", "redshift", "rhtml", "robot", "rst", "ruby", "rust", "sac", "sass", "scad", "scala", "scheme", "scrypt", "scss", "sh", "sjs", "slim", "smarty", "smithy", "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl", "terraform", "tex", "text", "textile", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript", "velocity", "verilog", "vhdl", "visualforce", "wollok", "xml", "xquery", "yaml", "zeek"]

btn_settings_editor_btns = [{
    "name": "copy",
    "feather": "Copy",
    "hasText": True,
    "alwaysOn": True,
    "commands": ["copyAll"],
    "style": {"top": "0rem", "right": "0.4rem"}
  },{
    "name": "update",
    "feather": "RefreshCw",
    "primary": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"bottom": "0rem", "right": "0.4rem"}
  }]

height = [19, 22]
language=choosen_langage
theme="default"
shortcuts="vscode"
focus=False
wrap=True
btns = custom_buttons_alt

theme = st.selectbox("theme:", ["dark", "light", "contrast"])


# with st.expander("Settings"):
col_a, col_b, col_c, col_cb = st.columns([6,11,3,3])
col_c.markdown('<div style="height: 2.5rem;"><br/></div>', unsafe_allow_html=True)
col_cb.markdown('<div style="height: 2.5rem;"><br/></div>', unsafe_allow_html=True)

# height_type = col_a.selectbox("height format:", ["css", "max lines", "min-max lines"], index=2)
# if height_type == "css":
#     height = col_b.text_input("height (CSS):", "400px")
# elif height_type == "max lines":
#     height = col_b.slider("max lines:", 1, 40, 22)
# elif height_type == "min-max lines":
# height = col_b.slider("min-max lines:", 1, 40, (19, 22))

col_d, col_e, col_f = st.columns([1,1,1])
language = choosen_langage
    # theme = col_e.selectbox("theme:", ["default", "light", "dark", "contrast"])
    # shortcuts = col_f.selectbox("shortcuts:", ["emacs", "vim", "vscode", "sublime"], index=2)
    # focus = col_c.checkbox("focus", False)
    # wrap = col_cb.checkbox("wrap", True)

with st.expander("Components"):
#     c_buttons = st.checkbox("custom buttons (JSON)", True)
#     if c_buttons:

    code_editor(json.dumps(custom_buttons_alt, indent=2), lang="json", height = 8, buttons=btn_settings_editor_btns)

# if response_dict_btns['type'] == "submit" and len(response_dict_btns['text']) != 0:
#     btns = json.loads(response_dict_btns['text'])
    # else:
    #     btns = []
        
    # i_bar = st.checkbox("info bar (JSON)", False)
    # if i_bar:
    #     response_dict_info = code_editor(json.dumps(info_bar, indent=2), lang="json", height = 8, buttons=btn_settings_editor_btns)
    
    #     if response_dict_info['type'] == "submit" and len(response_dict_info['text']) != 0:
    #         info_bar = json.loads(response_dict_info['text'])
    # else:
    #     info_bar = {}

st.write("### Output:")
# construct props dictionary (->Ace Editor)
ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}
response_dict = code_editor(ret,  height = height, lang=language, theme=theme, shortcuts=shortcuts, focus=focus, buttons=btns, info=info_bar, props=ace_props, options={"wrap": wrap}, allow_reset=True, key="code_editor_demo")

if response_dict['type'] == "submit" and len(response_dict['id']) != 0 and choosen_langage == "python":
    btns = response_dict["text"]
    update_database(prompt=Prompt, result=ret, new_result=btns, name=name) # update_database(prompt=Prompt, result=ret, new_result=btns, name=name)
    excecuter(str(btns))
elif choosen_langage == "python":
    excecuter(ret)
else:
    st.write("Désolé, on ne peut pas excécuter le {}.".format(choosen_langage))

close_connection(client)
