<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Insiares/Projet-NLT">
    <img src="Prototype_NLT/images/logo.png" alt="Logo"  height="200">
  </a>

<h3 align="center">NLT : A swing at Natural Langage Transcoder</h3>

  <p align="center">
    Our first aI pOwErEd app, helping noob programmers like us.
    <br />
    <br />
    <a href="https://github.com/Insiares/Projet-NLT/issues">Report Bug</a>
    ·
    <a href="https://github.com/Insiares/Projet-NLT/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


Our first local application, asking OpenAI-API to write code for us. The NLT should provide code corresponding to your prompt, allowing you to save it and edit it. If you ask for python code, you may be able to run it! <br>
<br>
We made this for school as a way to hone our wobbly skills, and it shows.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-shield]][Python-url]
* [![Streamlit][Streamlit-shield]][Streamlit-url]
* [![OpenAI][GPT-shield]][GPT-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.
You'll need python and docker to run this properly.

### Prerequisites

You should possess an OpenAI API key, and have it in your environnement variable under 'OPENAI_API_KEY'.


* For Windows, inside a command prompt : 
  ```sh
  setx OPENAI_API_KEY "your-api-key-here"
  ```

* Others : 
  ```sh
  export OPENAI_API_KEY='your-api-key-here'
  ```

_In case we were dumb enough to miss a step, please refer to [OpenAI API documentation](https://platform.openai.com/docs/quickstart )._

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/Insiares/Projet-NLT.git
   ```
3. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
4. Get the docker running
   ```sh
   cd ./Prototype_NLT/
   docker context create compose
   docker-compose -f docker-compose.yml up -d
   ```
4. CD into your /Prototype_NLT/ directory, and run the app inside your browser
   ```py
   streamlit run app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Enter your demand in the first text area, if you modify it and want to ask again, don't forget to validate by hitting CTRL+Enter.

The outputed code is displayed below in an editor. You can play with the code, and even run it (If giant pasta god's willing). If you want to keep your code for further use, hit run at least once to save it inside the database. 

You can then load previous session in the left sidebar. Choose your prompt and load it.

Might still be buggy, you can [open an issue](https://github.com/Insiares/Projet-NLT/issues).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Prototype
- [x] Session Recording
- [X] Save-enabled editable code block.
- [X] Execute outputed code.
- [~] Prompt Engineering
    - [~] More Langages
    - [ ] Different assistant personality

See the [open issues](https://github.com/Insiares/Projet-NLT/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

You shall not feel the need to. 

Should the extrem necessity emerges, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
6. Leave Star on your way out !

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Please don't.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Adrien for the awesome brief](https://github.com/dtrckd)
* [Antony for showing us the ropes of streamlit](https://github.com/DeVerMyst)
* [The genius who made the IA cover of Bloody Stream by Johnny Halliday, allowing me to maintain my sanity](https://www.youtube.com/watch?v=FIfvL6Wx3QM)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Insiares/Projet-NLT.svg?style=for-the-badge
[contributors-url]: https://github.com/Insiares/Projet-NLT/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Insiares/Projet-NLT.svg?style=for-the-badge
[forks-url]: https://github.com/Insiares/Projet-NLT/network/members
[stars-shield]: https://img.shields.io/github/stars/Insiares/Projet-NLT.svg?style=for-the-badge
[stars-url]: https://github.com/Insiares/Projet-NLT/stargazers
[issues-shield]: https://img.shields.io/github/issues/Insiares/Projet-NLT.svg?style=for-the-badge
[issues-url]: https://github.com/Insiares/Projet-NLT/issues
[license-shield]: https://img.shields.io/github/license/Insiares/Projet-NLT.svg?style=for-the-badge
[license-url]: https://github.com/Insiares/Projet-NLT/blob/master/LICENSE.txt
[GPT-shield]:https://img.shields.io/badge/chatGPT-74aa9c?logo=openai&logoColor=white
[GPT-url]:https://openai.com/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Python-shield]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]:https://www.python.org/
[Streamlit-shield]:https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[Streamlit-url]:https://streamlit.io/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
