import streamlit as st 
from Components.Call_API import call_gpt
from Components.utils_streamlit import variable_session, run_disable, enable
from time import time
from Database.mongodb import insert_in_database, get_database, close_connection, update_database
import sys
from io import StringIO
from code_editor import code_editor
import json
# ----------------------- session state declaration -----------------------
if 'prompt' not in st.session_state:
    st.session_state.prompt = ' '

if 'running' not in st.session_state:
    st.session_state.running = False

if 'result' not in st.session_state:
    st.session_state.result = ' '

if 'name' not in st.session_state:
    st.session_state.name = 'anon'

def excecuter(retour=st.session_state.result):
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    try:
        if st.session_state.result:
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



# ------------------------- App Layout ------------------------------------
#title
st.title('NLT By LesNuls')

#Sidebar
with st.sidebar: 
    sessions, client = get_database(st.session_state.name)
    list_session_prompt = [str(y['prompt'][:25]+'...') for y in sessions]

    if st.button('Reset'):
        st.session_state.result = ' '
        st.session_state.prompt = ' '
        list_session_prompt.insert(0, 'Empty Prompt')

    st.subheader('Sessions')

    st.text_input(label= 'Your Name',
                    # label_visibility='hidden',
                         placeholder=f"Enter your name", 
                         value='Anonyme',
                         key='name')
   
    option = st.radio(label='Select Past Prompt',options=[y for y in list_session_prompt])

    # if option is not None:
    #     selected_index = list_session_prompt.index(option)
    #     ret_, nom, prompt_ = variable_session((selected_index), st.session_state.name)
    #     st.session_state.result =ret_
    #     st.session_state.prompt = prompt_

    if st.button('Load'):
        if option is not None:
            selected_index = list_session_prompt.index(option)
            ret_, nom, prompt_ = variable_session((selected_index), st.session_state.name)
            st.session_state.result =ret_
            st.session_state.prompt = prompt_

        if option is None:
            list_session_prompt.insert(0, 'Empty Prompt')
            st.session_state.result = ' '
            st.session_state.prompt = ' '
    theme = st.selectbox("theme:", ["dark", "light", "contrast"])

    #Select lang
    choosen_langage = st.selectbox(
        'Choisissez votre langage',
        ('python', 'JS', 'C'))
    language = choosen_langage 

    # with st.expander("Settings"):
    col_a, col_b, col_c, col_cb = st.columns([6,11,3,3])
    col_c.markdown('<div style="height: 2.5rem;"><br/></div>', unsafe_allow_html=True)
    col_cb.markdown('<div style="height: 2.5rem;"><br/></div>', unsafe_allow_html=True)

    col_d, col_e, col_f = st.columns([1,1,1])
    
    


    
#Input Area for prompt
st.text_area(
             label_visibility='visible',
             value=st.session_state.prompt,
             key='prompt',
             on_change=enable,
             label= '''Enter your demand in this area, 
             if you modify it and want to ask again, 
             don't forget to validate by hitting CTRL+Enter''',)

if st.button(label='Generate', on_click=run_disable, disabled=st.session_state.running):
    with st.spinner('Working AI magic...'):
        st.session_state.result = call_gpt(st.session_state.prompt)
        st.success('Done!', icon='✅')
        insert_in_database(st.session_state.prompt, st.session_state.result, st.session_state.name)
        sessions, client = get_database(st.session_state.name)
        close_connection(client)

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




with st.expander("Components"):

    code_editor(json.dumps(custom_buttons_alt, indent=2), lang="json", height = 8, buttons=btn_settings_editor_btns)


st.write("### Output:")
st.write('You can edit your code, run it to save changes.')
# construct props dictionary (->Ace Editor)
ace_props = {"style": {"borderRadius": "0px 0px 8px 8px"}}
response_dict = code_editor(st.session_state.result,  height = height, lang=language, theme=theme, shortcuts=shortcuts, focus=focus, buttons=btns, info=info_bar, props=ace_props, options={"wrap": wrap}, allow_reset=True, key="code_editor_demo")

st.write("### Result:")
if response_dict['type'] == "submit" and len(response_dict['id']) != 0 and choosen_langage == "python":
    btns = response_dict["text"]
    update_database(prompt=st.session_state.prompt, result=st.session_state.result, new_result=btns, name=st.session_state.name) # update_database(prompt=Prompt, result=ret, new_result=btns, name=name)
    excecuter(str(btns))
elif choosen_langage == "python":
    excecuter(st.session_state.result)
else:
    st.write("Désolé, on ne peut pas excécuter le {}.".format(choosen_langage))

close_connection(client)