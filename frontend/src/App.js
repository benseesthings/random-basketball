import React, { useState } from "react";
import "./App.css";

export default function App() {
    const [playerData, setPlayerData] = useState(null);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const fetchPlayer = async () => {
        try {
            setLoading(true);
            setError("");
            setPlayerData(null);

            const res = await fetch("http://127.0.0.1:8080/player");
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const data = await res.json();
            setPlayerData(data);
        } catch (e) {
            setError(String(e));
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="App">
            <h1 className="title">Random Basketball Player</h1>

            <div className="actions">
                <button className="button" onClick={fetchPlayer}>
                    {loading ? "Loading…" : "Get Player"}
                </button>
            </div>

            {error && <p style={{ color: "red" }}>Error: {error}</p>}

            {playerData && (
                <div className="content">
                    {playerData.image_url && (
                        <img
                            className="player-img"
                            src={playerData.image_url}
                            alt={playerData.player}
                            onError={(e) => (e.currentTarget.style.display = "none")}
                        />
                    )}

                    <div className="card">
                        <h2>{playerData.player}</h2>
                        <p><strong>Points:</strong> {playerData.points}</p>
                        <p><strong>Assists:</strong> {playerData.assists}</p>
                        <p><strong>Years Played:</strong> {playerData.years}</p>
                        <p><strong>Fun Fact:</strong> {playerData.fun_fact}</p>
                    </div>
                </div>
            )}
        </div>
    );
}
