# Legal-GPT Frontend Interface

Pure frontend interface built with HTML, CSS, and JavaScript for the Legal-GPT platform.

## Features

- **Modern Design**: Legal/serious style combined with smart city aesthetic
- **Smooth Animations**: Clean, polished animations throughout
- **US Legal Provisions**: Comprehensive database of US legal provisions
- **Landmark Cases**: Analysis of significant Supreme Court decisions
- **Legal Consultation**: AI-powered legal question answering interface
- **Fully Responsive**: Works on desktop, tablet, and mobile devices

## File Structure

```
static/
├── index.html      # Main HTML file
├── styles.css       # Stylesheet with animations and themes
├── app.js          # JavaScript logic and data
└── README.md       # This file
```

## Setup

1. Simply open `index.html` in a modern web browser
2. Or serve via a web server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx http-server -p 8000
   
   # Using PHP
   php -S localhost:8000
   ```

3. Navigate to `http://localhost:8000` in your browser

## API Integration

To connect the frontend to your backend API:

1. Edit `app.js` and update the `API_CONFIG` object:
   ```javascript
   const API_CONFIG = {
       baseURL: 'http://your-api-url:port',
       endpoint: '/api/predict'
   };
   ```

2. Uncomment and modify the `callLegalAPI` function in `app.js` to match your API structure.

## Sections

### Legal Consultation
- Interactive legal question answering
- Configurable generation parameters
- Real-time AI analysis

### Legal Provisions
- Filter by category
- Constitutional Law
- Criminal Law
- Civil Rights
- Contract Law
- Tort Law

### Landmark Cases
- Supreme Court decisions
- Case summaries
- Key legal holdings

### About
- Platform information
- Technology stack
- Disclaimers

## Customization

### Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #0ea5e9;
    --secondary-color: #f59e0b;
    --accent-color: #8b5cf6;
    /* ... */
}
```

### Legal Data
Add or modify legal provisions and cases in `app.js`:
- `US_LEGAL_PROVISIONS` object
- `LANDMARK_CASES` array

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Opera

## Notes

- The interface uses modern CSS features (CSS Grid, Flexbox, CSS Variables)
- Animations use CSS transitions and keyframes
- No external dependencies required (pure HTML/CSS/JS)
- API integration requires CORS configuration on backend

## License

See main project LICENSE file.

