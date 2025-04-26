<!-- source: https://ui.nuxt.com/components/chat-prompt --> # ChatPromptPRO

[Textarea](/components/textarea)[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/ChatPrompt.vue)

An enhanced Textarea for submitting prompts in AI chat interfaces.

## Usage

The ChatPrompt component renders a `<form>` element and extends the
[Textarea](/components/textarea) component so you can pass any property such
as `icon`, `placeholder`, `autofocus`, etc.

GPT-4o

The ChatPrompt handles the following events:

  * The form is submitted when the user presses `↵` or when the user clicks on the submit button.
  * The textarea is blurred when `⎋` is pressed and emits a `close` event.

### Variant

Use the `variant` prop to change the style of the prompt. Defaults to
`outline`.

variant

soft

    
    
    <template>
      <UChatPrompt variant="soft" />
    </template>
    

## Examples

[](https://sdk.vercel.ai/docs/getting-started/nuxt)These chat components are
designed to be used with the `useChat` composable from **Vercel AI SDK**.

[](https://github.com/nuxt-ui-pro/chat)Check out the source code of our **AI
Chat template** on GitHub for a real-life example.

### Within a page

Use the ChatPrompt component with the `useChat` composable to display a chat
prompt within a page.

Pass the `input` prop alongside the `error` prop to disable the textarea when
an error occurs.

pages/[id].vue

    
    
    <script setup lang="ts">
    import { useChat } from '@ai-sdk/vue'
    
    const { messages, input, handleSubmit, reload, stop, status, error } = useChat()
    </script>
    
    <template>
      <UDashboardPanel>
        <template #body>
          <UContainer>
            <UChatMessages :messages="messages" :status="status">
              <template #content="{ message }">
                <MDC :value="message.content" :cache-key="message.id" unwrap="p" />
              </template>
            </UChatMessages>
          </UContainer>
        </template>
    
        <template #footer>
          <UContainer>
            <UChatPrompt v-model="input" :error="error" @submit="handleSubmit">
              <UChatPromptSubmit :status="status" @stop="stop" @reload="reload" />
            </UChatPrompt>
          </UContainer>
        </template>
      </UDashboardPanel>
    </template>
    

You can also use it as a starting point for a chat interface.

pages/index.vue

    
    
    <script setup lang="ts">
    const input = ref('')
    const loading = ref(false)
    
    async function onSubmit() {
      loading.value = true
    
      const chat = await $fetch('/api/chats', {
        method: 'POST',
        body: { input }
      })
    
      navigateTo(`/chat/${chat.id}`)
    }
    </script>
    
    <template>
      <UDashboardPanel>
        <template #body>
          <UContainer>
            <h1>How can I help you today?</h1>
    
            <UChatPrompt v-model="input" :status="loading ? 'streaming' : 'ready'" @submit="onSubmit">
              <UChatPromptSubmit />
            </UChatPrompt>
          </UContainer>
        </template>
      </UDashboardPanel>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'form'`| `any`  
`autofocus`| `true`| `boolean`  
`autoresize`| `true`| `boolean`  
`rows`| `1`| ` number`  
`icon`| | ` string`Display an icon based on the `leading` and `trailing` props.  
`error`| | ` Error`  
`modelValue`| | ` string`  
`variant`| `'outline'`| ` "outline" | "soft" | "subtle" | "naked"`  
`loading`| | `boolean`When `true`, the loading icon will be displayed.  
`loadingIcon`| `appConfig.ui.icons.loading`| ` string`The icon when the
`loading` prop is `true`.  
`avatar`| | ` AvatarProps`Display an avatar on the left side.Show properties

  * `as?: any`The element or component this component should render as. Defaults to `'span'`.
  * `src?: string`
  * `alt?: string`
  * `icon?: string`
  * `text?: string`
  * `size?: "md" | "xs" | "sm" | "lg" | "xl" | "3xs" | "2xs" | "2xl" | "3xl"`Defaults to `'md'`.
  * `class?: any`
  * `style?: any`
  * `ui?: { root?: ClassNameValue; image?: ClassNameValue; fallback?: ClassNameValue; icon?: ClassNameValue; }`

  
`placeholder`| `t('chatPrompt.placeholder')`| ` string`The placeholder text
for the textarea.  
`autofocusDelay`| | ` number`  
`autoresizeDelay`| | ` number`  
`maxrows`| | ` number`  
`ui`| | ` { root?: ClassNameValue; header?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; base?: ClassNameValue; } & { ...; }`Show properties

  * `root?: ClassNameValue`
  * `header?: ClassNameValue`
  * `body?: ClassNameValue`
  * `footer?: ClassNameValue`
  * `base?: ClassNameValue`
  * `leading?: ClassNameValue`
  * `leadingIcon?: ClassNameValue`
  * `leadingAvatar?: ClassNameValue`
  * `leadingAvatarSize?: ClassNameValue`
  * `trailing?: ClassNameValue`
  * `trailingIcon?: ClassNameValue`

  
  
### Slots

Slot |  Type   
---|---  
`header`| `{}`  
`footer`| `{}`  
`leading`| `{}`  
`default`| `{}`  
`trailing`| `{}`  
  
### Emits

Event |  Type   
---|---  
`close`| `[event: Event]`  
`submit`| `[event: Event]`  
`update:modelValue`| `[value: string]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        chatPrompt: {
          slots: {
            root: 'relative flex flex-col items-stretch gap-2 px-2.5 py-2 w-full rounded-lg backdrop-blur',
            header: 'flex items-center gap-1.5',
            body: 'items-start',
            footer: 'flex items-center justify-between gap-1.5',
            base: 'text-base/5'
          },
          variants: {
            variant: {
              outline: {
                root: 'bg-default/75 ring ring-default'
              },
              soft: {
                root: 'bg-elevated/50'
              },
              subtle: {
                root: 'bg-elevated/50 ring ring-default'
              },
              naked: {
                root: ''
              }
            }
          },
          defaultVariants: {
            variant: 'outline'
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
            chatPrompt: {
              slots: {
                root: 'relative flex flex-col items-stretch gap-2 px-2.5 py-2 w-full rounded-lg backdrop-blur',
                header: 'flex items-center gap-1.5',
                body: 'items-start',
                footer: 'flex items-center justify-between gap-1.5',
                base: 'text-base/5'
              },
              variants: {
                variant: {
                  outline: {
                    root: 'bg-default/75 ring ring-default'
                  },
                  soft: {
                    root: 'bg-elevated/50'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default'
                  },
                  naked: {
                    root: ''
                  }
                }
              },
              defaultVariants: {
                variant: 'outline'
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
            chatPrompt: {
              slots: {
                root: 'relative flex flex-col items-stretch gap-2 px-2.5 py-2 w-full rounded-lg backdrop-blur',
                header: 'flex items-center gap-1.5',
                body: 'items-start',
                footer: 'flex items-center justify-between gap-1.5',
                base: 'text-base/5'
              },
              variants: {
                variant: {
                  outline: {
                    root: 'bg-default/75 ring ring-default'
                  },
                  soft: {
                    root: 'bg-elevated/50'
                  },
                  subtle: {
                    root: 'bg-elevated/50 ring ring-default'
                  },
                  naked: {
                    root: ''
                  }
                }
              },
              defaultVariants: {
                variant: 'outline'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ChatPaletteA chat palette to create a chatbot interface inside an
overlay.](/components/chat-palette)[ChatPromptSubmitA Button for submitting
chat prompts with automatic status handling.](/components/chat-prompt-submit)

