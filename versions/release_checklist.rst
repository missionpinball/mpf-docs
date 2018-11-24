MPF release checklist
=====================

What to do to make a MPF release?

* [ ] Update :docs:`release_notes` (mpf-docs repository dev branch)
* [ ] Create draft blog post in ``missionpinball-website`` repository (in ``_draft`` folder)
* Create ``a.bb.x`` branch (e.g. 0.50.x) and push it based on dev
** [ ] ``mpf`` repository
** [ ] ``mpf-mc`` repository
** [ ] ``mpf-monitor`` repository
** [ ] ``mpf-examples`` repository
* [ ] Create a.bb branch (e.g. 0.50) and push it based on latest branch in ``mpf-docs`` repository
* [ ] Add ``a.bb`` to versions on readthedocs and wait until it finished building
* Increase version to a.bb.0 on ``a.bb.x`` branch
** [ ] ``mpf`` repository
** [ ] ``mpf-mc`` repository
** [ ] ``mpf-monitor`` repository
* [ ] Set version to ``a.bb.x`` in ``mpf-mc`` repository in ``appveyor.yml``
* [ ] Wait until all builds pass
* Increase version to ``a.bb.0-dev0`` (``bb + 1`` or ``a + 1``) on dev branch
** [ ] ``mpf`` repository
** [ ] ``mpf-mc`` repository
** [ ] ``mpf-monitor`` repository
* Update ``latest`` branch on ``mpf-docs``
** [ ] Remove branch protection
** [ ] Push dev branch to latest (hard push)
** [ ] Set ``current_branch`` to ``a.bb.x`` in ``conf.py``
** [ ] Set branch in ``.travis.yml`` to ``a.bb.x``
** [ ] Remove ``--pre`` from install notes
** [ ] Readd branch protection
* Update ``dev`` branch on ``mpf-docs``
** [ ] Update version to next release
* Protect branches
** [ ] ``a.bb.x`` on ``mpf`` repository
** [ ] ``a.bb.x`` on ``mpf-mc`` repository
** [ ] ``a.bb.x`` on ``mpf-monitor`` repository
** [ ] ``a.bb.x`` on ``mpf-examples`` repository
** [ ] ``a.bb`` on ``mpf-docs`` repository
* [ ] Publish release post on forum
* [ ] Publish release post on pinside
* [ ] Publish release post on slack
* Delete pre releases on pypi
** [ ] ``mpf``
** [ ] ``mpf-mc``
** [ ] ``mpf-monitor``
