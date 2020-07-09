# Using Jupyter Notebook - Tips and Tricks



## Solve - Slow in Tab Autocompletion



Run following command at the top of Jupyter notebook.

```
%config Completer.use_jedi = False
```

Reference: https://stackoverflow.com/questions/44186370/kernel-taking-too-long-to-autocomplete-tab-in-jupyter-notebook

This also can be added permanently to IPython configuration.

1. Run following to find out IPython profile folder, e.g. `C:\Users\User\.ipython`

   ```
   import IPython
   IPython.paths.get_ipython_dir()
   ```

2. There will be following 2 config files in `profile_*` folder.

   * ipython_config.py
   * ipython_kernel_config.py

3. If above config files not exist, run following command to generate them.

   ```
   ipython profile create
   ```

4. Find the file `.\profile_default\ipython_config.py`, add following line to the file.

   ```
   c.Completer.use_jedi = True
   ```



## Make matplotlib inline

When working with matplotlib in Jupyter Notebook, it is common to run following command at the top of the notebook.
```
%matplotlib inline
```

With this command, the output of plotting commands is displayed inline within frontends like the Jupyter notebook, directly below the code cell that produced it. The resulting plots will then also be stored in the notebook document.

You can also set it in IPython profile so that it is always set.

1. Add following line to `ipython_kernel_config.py` in IPython profile folder.

```
c.InteractiveShellApp.matplotlib = "inline"
```

Reference: 
* https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline
* https://stackoverflow.com/questions/21176731/automatically-run-matplotlib-inline-in-ipython-notebook


## Presentation using RISE

[RISE](https://github.com/damianavila/RISE): "Live" Reveal.js Jupyter/IPython Slideshow Extension

1. Install RISE
   * For notebook cells set as **Slide** type, RISE show them as slides.
   * There is no built-in shortcut to set all slides to **Slide** type. We will setup a javascript in `custom.js` to provide a shortcut key. 
2. Create an `.jupyter\custom\custom.js` file with following content. This script will help to set cells into **Slide** type with shortcut key `shift-z`.
    ```
    define(
    ['base/js/namespace',
     'base/js/events'
    ],
    function(Jupyter, events) {
        // mark individual cell
        function set_slide(cell, bool) {
            let metadata = cell.metadata;
            if (metadata.slideshow === undefined){
                metadata.slideshow = {};
            }
	    metadata.slideshow.slide_type = bool ? 'slide' : undefined;
        }
        // mark all cells as Slide
        function mark_all_cells_as_slide() {
            Jupyter.notebook.get_cells().forEach(function(cell) {
                set_slide(cell, true);
            });
            // need to update the slideshow toolbar to reflect changes
            Jupyter.CellToolbar.rebuild_all();
        }
        // actually bind to a keyboard shortcut
        Jupyter.keyboard_manager.command_shortcuts.add_shortcut(
            'shift-z', // or alt-z or meta-z or similar
            { help : 'set the Slide tag on all cells',
              handler: mark_all_cells_as_slide,
            })
    })
    ```
3. Start Jupyter Notebook and open a notebook.
4. Press `shift-z` to set all cells as **Slide** type. (With script in step 2)
5. An button "Enter/Exit RISE Slideshow" will be added to Jupyter Notebook toolbar.
6. Click on the button to start slideshow.
   * Press Left/Right key to move from cell to cell
   * Scroll up/down if cell is too large to fit in screen
