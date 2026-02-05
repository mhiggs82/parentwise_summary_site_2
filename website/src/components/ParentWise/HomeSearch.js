import React from 'react';

export default function HomeSearch() {
    return (
        <div style={{
            maxWidth: '600px',
            margin: '0 auto 64px',
            position: 'relative',
            display: 'flex',
            gap: '8px'
        }}>
            <input
                type="text"
                placeholder="Search for guides, authors, or topics..."
                style={{
                    flex: 1,
                    background: 'var(--pw-bg-card)',
                    border: '1px solid var(--pw-border)',
                    borderRadius: '12px',
                    padding: '12px 20px',
                    color: 'white',
                    fontSize: '16px',
                    outline: 'none',
                    transition: 'all 0.2s ease'
                }}
                onFocus={(e) => e.target.style.borderColor = 'var(--pw-purple)'}
                onBlur={(e) => e.target.style.borderColor = 'var(--pw-border)'}
            />
            <button className="pw-button">Search</button>
        </div>
    );
}
