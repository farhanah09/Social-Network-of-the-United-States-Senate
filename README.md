# Social Network of the United States Senate

## Problem Description

The Senate is one of the two chambers in the legislative branch of the United States federal government. It comprises 100 members: two senators from each of the 50 states elected to a 6-year term. To pass, amend, or repeal a law, a member of Congress must introduce a bill, which describes the details of the new law or the proposed changes to the old law. In this project, we will explore the social network of the US Senate induced by bill co-sponsorship during the 116th Congress (January 3, 2019, to January 3, 2021).

## Data Sources

The data for this project were obtained from [GPO Bulk Data](https://www.gpo.gov/fdsys/bulkdata/BILLSTATUS/116). The following files are used:

- `senators.csv`: Contains the list of all Senators who served during the 116th Congress, including their name, state, party affiliation (R - Republican, D - Democrat, I - Independent), and an ID number from 1-1022. Also includes (x,y) coordinates corresponding to the latitude and longitude of points within each state.
- `senateCosponsorship.csv`: Contains a list of all pairs of Senators (referred to by their ID numbers) who have co-sponsored at least 8 bills together.

## Python Package Requirements

To run this project, you need to install the required packages from `requirements.txt`. You can do this using the following command:

```bash
pip install -r requirements.txt
