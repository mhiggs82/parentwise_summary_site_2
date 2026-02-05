import React from 'react';

export default function SophiaLogo({ size = 120 }) {
    return (
        <div style={{
            width: size,
            height: size,
            borderRadius: '50%',
            background: 'var(--pw-purple)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 0 30px var(--pw-purple-glow)',
            margin: '0 auto 24px'
        }}>
            <svg
                width={size * 0.6}
                height={size * 0.6}
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
            >
                <path
                    d="M12 22C12 22 20 18 20 12C20 6 12 2 12 2C12 2 4 6 4 12C4 18 12 22 12 22Z"
                    fill="white"
                    fillOpacity="0.2"
                />
                <path
                    d="M12 22C12 22 12 12 12 2M12 22C12 22 20 18 20 12C20 6 12 2 12 2M12 22C12 22 4 6 4 12C4 18 12 2 12 2"
                    stroke="white"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                />
                <circle cx="12" cy="12" r="3" fill="white" />
            </svg>
        </div>
    );
}
