#!/bin/bash
# Monitor GEMINI_FEEDBACK.md for Gemini responses
# Usage: ./monitor_gemini_feedback.sh

FEEDBACK_FILE="/home/king/Downloads/documentsforgi/GEMINI_FEEDBACK.md"
LAST_HASH=""

echo "🔄 Monitoring GEMINI_FEEDBACK.md for Gemini responses..."
echo "   Press Ctrl+C to stop"
echo ""

while true; do
    CURRENT_HASH=$(md5sum "$FEEDBACK_FILE" | cut -d' ' -f1)

    if [ "$CURRENT_HASH" != "$LAST_HASH" ]; then
        if [ -n "$LAST_HASH" ]; then
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "📝 GEMINI_FEEDBACK.md updated at $(date '+%Y-%m-%d %H:%M:%S')"
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

            # Check if Gemini section has content
            if grep -q "Responses from Gemini" "$FEEDBACK_FILE"; then
                GEMINI_SECTION=$(sed -n '/## Responses from Gemini/,/## Claude Follow-ups/p' "$FEEDBACK_FILE" | head -20)
                if echo "$GEMINI_SECTION" | grep -qv "Awaiting Gemini input"; then
                    echo ""
                    echo "🤖 NEW GEMINI RESPONSE DETECTED!"
                    echo ""
                    echo "$GEMINI_SECTION"
                    echo ""
                    echo "💡 Run Claude Code to process the response"
                fi
            fi
        fi
        LAST_HASH="$CURRENT_HASH"
    fi

    sleep 5
done
