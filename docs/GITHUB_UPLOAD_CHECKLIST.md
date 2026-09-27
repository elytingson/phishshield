# GitHub Upload Checklist

Before publishing:

- [ ] Replace `<YOUR-USERNAME>` in `CITATION.cff`
- [ ] Replace author placeholders in `CITATION.cff`
- [ ] Confirm the notebook outputs do not contain confidential URLs
- [ ] Confirm no raw dataset file is staged for commit
- [ ] Confirm no trained `.joblib` model is staged unless intentionally published
- [ ] Confirm presentation decks open correctly
- [ ] Run `pytest -q`
- [ ] Run Chapter 3 → Chapter 4 → Chapter 5 locally
- [ ] Set `FAST_MODE=False` for final reported metrics
- [ ] Update README with the final GitHub repository URL
- [ ] Create GitHub release/tag `v1.0.0` after final submission
