<!-- source: https://ui.nuxt.com/components/chat-palette --> # ChatPalettePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/ChatPalette.vue)

A chat palette to create a chatbot interface inside an overlay.

## Usage

The ChatPalette component is a structured layout wrapper that organizes
[ChatMessages](/components/chat-messages) in a scrollable content area and
[ChatPrompt](/components/chat-prompt) in a fixed bottom section, creating
cohesive chatbot interfaces for modals, slideovers, or drawers.

    
    
    <template>
      <UChatPalette>
        <UChatMessages />
    
        <template #prompt>
          <UChatPrompt />
        </template>
      </UChatPalette>
    </template>
    

## Examples

[](https://sdk.vercel.ai/docs/getting-started/nuxt)These chat components are
designed to be used with the `useChat` composable from **Vercel AI SDK**.

### Within a Modal

You can use the ChatPalette component inside a [Modal](/components/modal)'s
content.

    
    
    <script setup lang="ts">
    import { useChat } from '@ai-sdk/vue'
    
    const { messages, input, handleSubmit, status, error } = useChat()
    </script>
    
    <template>
      <UModal open :ui="{ content: 'sm:h-[28rem]' }">
        <template #content>
          <UChatPalette>
            <UChatMessages
              :messages="messages"
              :status="status"
              :user="{ side: 'left', variant: 'naked', avatar: { src: 'https://github.com/benjamincanac.png' } }"
              :assistant="{ icon: 'i-lucide-bot' }"
            >
              <template #content="{ message }">
                <MDC :value="message.content" :cache-key="message.id" unwrap="p" />
              </template>
            </UChatMessages>
    
            <template #prompt>
              <UChatPrompt
                v-model="input"
                icon="i-lucide-search"
                variant="naked"
                :error="error"
                @submit="handleSubmit"
              />
            </template>
          </UChatPalette>
        </template>
      </UModal>
    </template>
    

Expand code

### Within ContentSearch

You can use the ChatPalette component conditionally inside
[ContentSearch](/components/content-search)'s content to display a chatbot
interface when a user selects an item.

    
    
    <script setup lang="ts">
    import { useChat } from '@ai-sdk/vue'
    
    const groups = computed(() => [{
      id: 'ai',
      ignoreFilter: true,
      items: [{
        label: searchTerm.value ? `Ask AI for “${searchTerm.value}”` : 'Ask AI',
        icon: 'i-lucide-bot',
        onSelect: (e: any) => {
          e.preventDefault()
    
          ai.value = true
    
          if (searchTerm.value) {
            setMessages([{
              id: '1',
              role: 'user',
              content: searchTerm.value
            }])
    
            reload()
          }
        }
      }]
    }])
    
    const ai = ref(false)
    const searchTerm = ref('')
    
    const { messages, input, handleSubmit, status, error, reload, setMessages } = useChat()
    
    function onClose(e: Event) {
      e.preventDefault()
    
      ai.value = false
    }
    </script>
    
    <template>
      <ClientOnly>
        <LazyUContentSearch v-model:search-term="searchTerm" open :groups="groups">
          <template v-if="ai" #content>
            <UChatPalette>
              <UChatMessages
                :messages="messages"
                :status="status"
                :user="{ side: 'left', variant: 'naked', avatar: { src: 'https://github.com/benjamincanac.png' } }"
                :assistant="{ icon: 'i-lucide-bot' }"
              >
                <template #content="{ message }">
                  <MDC :value="message.content" :cache-key="message.id" unwrap="p" />
                </template>
              </UChatMessages>
    
              <template #prompt>
                <UChatPrompt
                  v-model="input"
                  icon="i-lucide-search"
                  variant="naked"
                  :error="error"
                  @submit="handleSubmit"
                  @close="onClose"
                />
              </template>
            </UChatPalette>
          </template>
        </LazyUContentSearch>
      </ClientOnly>
    </template>
    

Expand code

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`ui`| | ` { root?: ClassNameValue; prompt?: ClassNameValue; close?: ClassNameValue; content?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{}`  
`prompt`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        chatPalette: {
          slots: {
            root: 'relative flex-1 flex flex-col min-h-0 min-w-0',
            prompt: 'px-0 rounded-t-none border-t border-default',
            close: '',
            content: 'overflow-y-auto flex-1 flex flex-col py-3'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          uiPro: {
            chatPalette: {
              slots: {
                root: 'relative flex-1 flex flex-col min-h-0 min-w-0',
                prompt: 'px-0 rounded-t-none border-t border-default',
                close: '',
                content: 'overflow-y-auto flex-1 flex flex-col py-3'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          uiPro: {
            chatPalette: {
              slots: {
                root: 'relative flex-1 flex flex-col min-h-0 min-w-0',
                prompt: 'px-0 rounded-t-none border-t border-default',
                close: '',
                content: 'overflow-y-auto flex-1 flex flex-col py-3'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ChatMessagesDisplay a list of chat messages, designed to work seamlessly with
Vercel AI SDK.](/components/chat-messages)[ChatPromptAn enhanced Textarea for
submitting prompts in AI chat interfaces.](/components/chat-prompt)

