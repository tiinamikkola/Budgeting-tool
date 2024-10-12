## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://version.aalto.fi/gitlab/mikkolt7/y2_2023_24674.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://version.aalto.fi/gitlab/mikkolt7/y2_2023_24674/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

## Name
Rahan seuranta (Y2 projekti)

## Maker
Tiina Mikkola (tiina.m.mikkola@aalto.fi)

## Description
Ohjelma, joka lukee tilitapahtumat tiedostosta (.csv), erottelee tulot ja menot toisistaan sekä taulukoi menot ja tulot.

## Usage
1.Aja main.py

2.Anna oikea tilitapahtumatiedosto (.csv). Voit käyttää esimerkkitiedostoa tilitapahtuma.csv. Huomaa, että tilitapahtumatiedoston on oltava oikeanlainen (OP:n verkkopanista ladattava csv-tiedosto).

3.Seuraa ohjelman antamia ohjeita ryhmitelläksesi tapahtumia, tulostaaksesi tulokset tai lopettaaksesi ohjelman ajaminen. Ohjelman ajo loppuu valitsemalla exit-vaihtoehto (6) sitä kysyttäessä.