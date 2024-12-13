# Sagnik Chakraborty's Lab Notebook 

This repo contains an MDbook containing all of my lab notes so that it is easier to read in book format. 

## Installation 
First, ensure you install rust to your system. Follow the directions on the 
[rust installation page](https://www.rust-lang.org/tools/install) to install the required tools, `rust` and `cargo`. 
If you're on MacOS or a linux based system, you can just run 

```sh 
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
After you have access to the `cargo` command, run 
`cargo install mdbook`, followed by `cargo install mdbook-katex`

If you're a windows user, [install mdbook-katex with these instructions](https://github.com/lzanini/mdbook-katex)

Then after cloning the repository, all you need to do is head into the folder where this 
README file is (should be called `Sagnik3_notebook/`) and type 

```sh
mdbook serve --open
```

Then navigate to http://localhost:3000 in your browser. 

If you have any trouble anyways, the book is going to all be in markdown format anyways, so you can head into the `src/` directory to see the .md pages
For more help, see [this link](https://rust-lang.github.io/mdBook/guide/installation.html) for info about installing mdbook into your system.





