# Single-Page CV

## Project URL

This project is based on the roadmap.sh Single-Page CV challenge: [https://roadmap.sh/projects/single-page-cv](https://roadmap.sh/projects/single-page-cv).

A simple, single-page CV built with HTML and CSS. It displays personal information, skills, education, work experience, and links to online profiles. The page also includes basic metadata for browsers and search engines.

## Project Structure

Keep the HTML file and favicon file in the same folder if you want the current relative favicon path to work:

```text
single-page-cv/
├── index.html
├── favicon.svg
└── README.md
```

The HTML file can have a different name, but `favicon.svg` should be in the location referenced by the `href` attribute in the HTML.

## How It Works

### 1. HTML document setup

- `<!doctype html>` tells the browser to use modern HTML standards.
- `<html lang="en">` marks the document language as English.
- `<meta charset="UTF-8">` sets the character encoding so text and symbols display properly.
- The viewport meta tag helps the page scale to different screen sizes, including mobile devices.
- `<title>Single-Page CV</title>` sets the text shown in the browser tab and may be used as the title in search results.

### 2. Favicon

This line references the icon file:

```html
<link rel="icon" type="image/png" href="favicon.svg" />
```

The browser looks for `favicon.svg` relative to the HTML file. Make sure that file exists at the expected path. The current `type` says PNG while the filename ends in `.svg`; the declared type should match the actual icon format if the browser does not display it reliably. This note is documentation only; the HTML has not been changed.

### 3. SEO and social-sharing metadata

- `description` provides a brief summary of the page that search engines may use in search previews.
- `keywords` lists terms related to the page. Major search engines such as Google generally do not use the keywords meta tag for ranking.
- `og:title` defines the title that can be used when the page is shared on platforms that support Open Graph metadata.

These tags help describe the page, but they do not guarantee that a search engine will index it or display the exact metadata provided.

### 4. CSS styling

The `<style>` block contains the page's CSS:

- The universal selector (`*`) removes default margin and padding and sets `box-sizing: border-box` for more predictable element sizing.
- `body` sets the font to Arial/Helvetica and adds spacing around the page content with `padding: 5.5rem`.
- `.header` makes section labels green.
- `.title` makes the education and experience heading text blue.

The CSS is embedded in the HTML file, so there is no separate stylesheet to install or link.

### 5. CV content

The `<body>` contains the visible CV:

- **Name and role:** your name and the “Junior Frontend Developer” label.
- **Contact details:** location, phone number, and email.
- **Skills:** a line listing technical and design skills.
- **Education:** school, degree, dates, and a list of activities or learning outcomes.
- **Experience:** organization, role or placement dates, responsibilities, and skills gained.
- **Across the Internet:** LinkedIn and GitHub profile addresses.

The page uses headings, paragraphs (`<p>`), spans (`<span>`), and lists (`<ul>` and `<li>`) to organize the content. The `<br>` elements add manual line breaks and spacing.

## How to Run It

1. Save the HTML code in a file such as `index.html`.
2. Put `favicon.svg` in the location referenced by the HTML.
3. Open `index.html` in a web browser by double-clicking it, or use the Live Server extension in Visual Studio Code for local previewing.
4. Edit the existing HTML text to update CV details. Adjust the CSS rules in the `<style>` block to change colors, fonts, and spacing.

No JavaScript, package installation, or build step is required for this page.

## Notes

- Keep personal details accurate and only publish contact information you are comfortable making public.
- Update the LinkedIn and GitHub addresses to your actual profile URLs.
- The project is a static page. It does not include a database, form submission, or backend server.
