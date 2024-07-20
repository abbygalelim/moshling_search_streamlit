# Moshling Search Streamlit by Blueshift

Are you an avid Moshi Online user and moshling hunter? Did you wish that you had a fast and clean way of looking up moshlings, their seed combinations, and other stats? Well look no further, as this Streamlit application has all of the features for you!

## Pages

### Home

A summary of the moshlings you own in your garden.

- `Your wishlist`: keep note of the moshling you are currently trying to catch. Double click `Show Wishlist` or `Hide Wishlist` button to show or hide this feature.
- `Moshlings in your garden`: view the number of moshlings you own and a table of the moshlings' information. The information provided include their name, what set they belong to, whether you own them or not, their rarity, and the color and type of seeds that they require. You can click the title of each column to sort the table by that column.
- `Stats`: view the number and names of the sets that are completed (you own all of the moshlings in that set), almost complete (you are one moshling away from completing that set), and empty (you do not own any moshlings in that set).

### Moshling Seed Combo Search

View the moshlings that are attracted by the seeds you specify.

You can search up moshlings based on 1, 2, or 3 seeds. This page will generate results once at least one `Seed` selection is filled. You can further specify by color.

- `Type of Results`
  - `General` will list moshlings that match the requirements you specify in a general sense. If you search `Blue Dragon Fruit`, the page will not only list moshlings that require a `Blue Dragon Fruit` but also moshlings that require `Any Dragon Fruit`, since `Blue` fufils the requirement `Any`. Similarly, if you search `Any Crazy Daisy`, the page will list moshlings that require `Any Crazy Daisy` and any color variation of `Crazy Daisy`.
  - `Specific` will only show the moshlings that require the exact seeds you list. The moshlings that will show up for `Red Love Berries` and `Any Magic Beans` are the moshlings that have those exact seeds in their combination.

### Moshling Name and Search Set

View information on moshlings you search by set or name.

- `Search by Set`: select a set from the dropdown list to view a table of information on all of the moshlings within that set.
- `Search by Name`: enter a word or letters to generate a table of information on all of the moshlings that have those letters in their name. For example, searching `Roxy` will show you `Roxy`, `H. Roxy`, `S. Roxy`, and `C. Roxy`.

### Rarity Search

View moshlings based on their rarity

- `Choose a Rarity`: select a rarity from the dropdown list to view a table of information on all of the moshlings under that rarity. The number of moshlings you own within that rarity and number of moshlings you do not own are also listed.
- `Filter by Owned`: further limit your search by selecting `Owned` to only view the moshlings within that rarity that you have in your garden or `Not Owned` to see the ones you do not have. Leave that selection blank if you wish to view both.

### Edit Garden

Add or remove moshlings from your garden

- `Choose a moshling`: select the moshling you would like to add or remove from your garden.
- Double click `Add` or `Remove` to add or remove the selected moshling. You can also navigate to the `Home` page to see that moshling now listed in your garden.

### Help

View path to where you have `moshling_search_streamlit` and `garden.csv` stored in your files. There is also a link back to this README.md.

## Getting Started

Once you have this repo cloned and the application up and running (see Local Installation below), you are ready to search through your moshlings!

As long as you have a terminal window open running `streamlit run app/Home.py`, the application will work. If you ever close your terminal, just reopen a terminal window, navigate to the `moshling_search_streamlit` folder, and run `streamlit run app/Home.py`.

There is no need to touch any of the files within this folder. Everything you need can be accessed through the browser application. The only time where you would want to directly edit a file is if you want to update all the moshlings you have in your garden at once, right after downloading this repo.

### Initializing your Garden (right after downloading this repo):

The file `garden.csv` (full path can be found in the `Help` page) keeps track of all of your owned moshlings. As a default, that file lists all 306 moshlings as not owned. You have two options of how to update this file:

- From the browser (safer option):
  - On the left menu, click on `Edit Garden`
  - Select the moshling you would like to add or remove from your garden
  - Click `Add` or `Remove` to add or remove the selected moshling
  - Click the same `Add` or `Remove` button again to see the changes take place. You can also navigate to the `Home` page to see that moshling now listed in your garden.
- From the file (less safe but perhaps faster option):
  - Open up the file `garden.csv`, in which you will see each line consists of `[Moshling Name]`,`No`
  - For all of the moshlings you own, replace `No` with `Yes` (make sure `Yes` is capitalized and spelled exactly. Also ensure that no space is added before or after the comma)
  - Save the file. Navigate to the home page and you should see all of your moshlings listed in your garden.
    After this first update to your garden, the browser solution should be sufficient to add moshlings one by one as you collect them. The file method makes sense for bigger batches of additions or subtractions.

## Local Installation

Open a terminal window to complete these actions.

Prerequisites:
- Python: run `python --version` or python3 --version` to check if you have python installed. If not, download [here](https://www.python.org/downloads/).
- Pip: after installing Python, run `pip --version` to check if you have pip installed.
- Streamlit: after confirming you have python and pip, run `pip install streamlit` to install Streamlit. More info about that download process [here](https://docs.streamlit.io/get-started/installation/command-line).
- Git: run `git --version` to check if you have git installed. More info about that process [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Navigate to the place in your files where you would like to download this repo and then run `git clone https://github.com/abbygalelim/moshling_search_streamlit.git`.

Navigate inside of the folder you just cloned (`cd moshling_search_strealit`) and run `streamlit run app/Home.py`. This action will open up the app in your browser for you to use!
