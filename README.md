# License Plate Detection — Part 1
**Haar Cascade Training to produce `haar_carplate.xml`**

This repository contains the **first stage** of a two-part LPR system:

- **Part 1 (this repo):** Build a Haar feature cascade to **detect the plate ROI** and export `haar_carplate.xml`.
- **Part 2 (separate repo):** Character segmentation + CNN recognition. [→ Go to Part 2: Character Segmentation & CNN](https://github.com/lok-bit/license-plate-recognition)

> **Output:** `model/haar_carplate.xml`, used by Part-2 to crop plate regions.

---

## Pipeline (This Repo)

1. **Prepare Samples**  
   - Collect **positive** images (plates present) and **negative** images (no plates).  
   - Downscale very large images to a consistent size for training stability and speed.  
   - Unify formats (e.g., positives to **BMP**; negatives to **grayscale**).

2. **Annotate Positives**  
   - Use a bounding-box tool (e.g., `objectmarker`) to label plate boxes and export `annot/info.txt` in `x y w h` format.  
   - Manually review a batch of labels to ensure boxes are neither too tight nor too loose.

3. **(Optional) Data Augmentation**  
   - Light cropping/rotation/contrast variants to increase positive samples.  
   - Keep the plate box safely away from crop edges; update box coordinates accordingly.

4. **Create Negative List & Positive Vector**  
   - Generate `bg/bg.txt` listing every negative image (one path per line).  
   - Pack positives into a `.vec` file with `opencv_createsamples` (set `-num`, `-w`, `-h` to your dataset).

5. **Train Haar Cascade**  
   - Run `opencv_traincascade` with your chosen stage count and window size (e.g., `-numStages`, `-w`, `-h`, `-numPos`, `-numNeg`).  
   - Clear previous `training/cascades` outputs before re-training.

6. **Export Final Model**  
   - Convert training output to `model/haar_carplate.xml` (via your convert script or tool).

7. **Quick Validation**  
   - Run a small detection script on `data/test/` to visually confirm plate localization quality.

---

## Requirements

- **OpenCV** with `opencv_createsamples` and `opencv_traincascade`
- Python 3.x for helper scripts (optional)
- Pillow / NumPy (optional, for preprocessing utilities)

---

## Notes & Tips

- Consistent sizes & formats help the Haar features focus on intensity/edge contrasts.
- Label quality dominates results—review boxes; avoid cutting digits or background leakage.
- Choose a detection window ratio that roughly matches your plate geometry (new vs. old plate formats may differ).
- Keep negatives diverse (roads, cars without visible plates, backgrounds).

---

## Output

- model/haar_carplate.xml — the trained cascade model consumed by Part-2 for plate ROI cropping.

---

## Acknowledgements
- OpenCV (Haar features, training utilities)
- Community tutorials and tools for cascade training workflows
  
